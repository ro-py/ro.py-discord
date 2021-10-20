from .exceptions import BloxlinkError, RoVerError
from .partials import RoVerPartialUser

from typing import Union

from roblox import Client
from roblox.bases.baseuser import BaseUser
from roblox.users import User
from roblox.utilities.shared import ClientSharedObject
from roblox.utilities.requests import CleanAsyncClient


class VerificationClient:
    def __init__(
            self,
            client: Client,
            bloxlink_url: str = "blox.link",
            rover_url: str = "verify.eryn.io"
    ):
        """
        Parameters:
            client: A ro.py client.
            bloxlink_url: Base URL to use for Bloxlink API requests.
            rover_url: Base URL to use for RoVer API requests.
        """
        self._client: Client = client
        self._shared: ClientSharedObject = self._client._shared
        self._requests: CleanAsyncClient = CleanAsyncClient()

        self.bloxlink_url: str = bloxlink_url
        self.rover_url: str = rover_url

    async def get_user_bloxlink(self, user_id: int, expand: bool = True) -> Union[User, BaseUser]:
        """
        Gets a Roblox user from their Discord ID using the RoVer API.

        Parameters:
            user_id: The user's Discord ID.
            expand: Whether to return a User object (2 requests) rather than a RoVerPartialUser object (1 request)

        Returns:
            A `User` if `expand` is True, and a `BaseUser` otherwise.
        """

        user_response = await self._requests.get(
            url=self._shared.url_generator.get_url(
                subdomain="api",
                path=f"v1/user/{user_id}",
                base_url=self.bloxlink_url
            )
        )
        user_data = user_response.json()
        response_status = user_data["status"]
        response_status_ok = response_status == "ok"

        if not response_status_ok:
            # if the response was not OK, raise an error
            response_message = user_data["error"]
            raise BloxlinkError(f"{response_status}: {response_message}")

        user_id = int(user_data["primaryAccount"])
        if expand:
            return await self._client.get_user(user_id=user_id)
        else:
            return self._client.get_base_user(user_id=user_id)

    async def get_user_rover(self, user_id: int, expand: bool = True) -> Union[User, RoVerPartialUser]:
        """
        Gets a Roblox user from their Discord ID using the RoVer API.

        Parameters:
            user_id: The user's Discord ID.
            expand: Whether to return a User object (2 requests) rather than a RoVerPartialUser object (1 request)

        Returns:
            A `User` if `expand` is True, and a `RoVerPartialUser` otherwise.
        """
