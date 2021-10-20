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
            bloxlink_subdomain: str = "api",
            rover_url: str = "eryn.io",
            rover_subdomain: str = "verify"
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
        self.bloxlink_subdomain: str = bloxlink_subdomain
        self.rover_url: str = rover_url
        self.rover_subdomain: str = rover_subdomain

    async def get_user_bloxlink(self, user_id: int, expand: bool = True) -> Union[User, BaseUser]:
        """
        Gets a Roblox user from their Discord ID using the RoVer API.

        Parameters:
            user_id: The user's Discord ID.
            expand: Whether to return a User object (2 requests) rather than a RoVerPartialUser object (1 request)

        Returns:
            A `User` if `expand` is True, and a `BaseUser` otherwise.
        """

        bloxlink_response = await self._requests.get(
            url=self._shared.url_generator.get_url(
                subdomain=self.bloxlink_subdomain,
                path=f"v1/user/{user_id}",
                base_url=self.bloxlink_url
            )
        )
        bloxlink_data = bloxlink_response.json()
        response_status = bloxlink_data["status"]
        response_status_ok = response_status == "ok"

        if not response_status_ok:
            # if the response was not OK, raise an error
            response_message = bloxlink_data["error"]
            raise BloxlinkError(f"{response_status}: {response_message}")

        user_id = int(bloxlink_data["primaryAccount"])
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
        rover_response = await self._requests.get(
            url=self._shared.url_generator.get_url(
                subdomain=self.rover_subdomain,
                path=f"/api/user/{user_id}",
                base_url=self.rover_url
            )
        )
        rover_data = rover_response.json()
        response_status = rover_data["status"]
        response_status_ok = response_status == "ok"

        if not response_status_ok:
            # if the response was not OK, raise an error
            response_message = rover_data["error"]
            raise RoVerError(f"{rover_response.status_code}: {response_message}")

        if expand:
            return await self._client.get_user(user_id=rover_data["robloxId"])
        else:
            return RoVerPartialUser(
                shared=self._shared,
                data=rover_data
            )
