from .exceptions import BloxlinkError

from typing import Union

from roblox import Client
from roblox.bases.baseuser import BaseUser
from roblox.users import User
from roblox.utilities.shared import ClientSharedObject
from roblox.utilities.requests import Requests


class BloxlinkClient:
    def __init__(self, client: Client, base_url: str = "blox.link"):
        """
        Parameters:
            client: A ro.py client.
            base_url: The base URL.
        """
        self._client: Client = client
        self._shared: ClientSharedObject = self._client._shared
        self._requests: Requests = self._shared.requests

        self.base_url: str = base_url

    async def get_user(self, user_id: int, expand: bool = True) -> Union[User, BaseUser]:
        """
        Parameters:
            user_id: The Discord user's ID.
            expand: Whether to convert the object into a full User object.
        """
        user_response = await self._requests.get(
            url=self._shared.url_generator.get_url(
                subdomain="api",
                path=f"v1/user/{user_id}",
                base_url=self.base_url
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
