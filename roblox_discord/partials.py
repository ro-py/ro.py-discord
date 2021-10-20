from roblox.utilities.shared import ClientSharedObject
from roblox.bases.baseuser import BaseUser


class RoVerPartialUser(BaseUser):
    """
    Represents a partial user, as returned from RoVer's Discord-to-Roblox API endpoint.
    """
    def __init__(self, shared: ClientSharedObject, data: dict):
        self._shared: ClientSharedObject = shared
        self.id: int = data["robloxId"]
        super().__init__(
            shared=self._shared,
            user_id=self.id
        )
        self.name: str = data["robloxUsername"]
