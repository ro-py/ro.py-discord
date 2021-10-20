import asyncio
from roblox import Client
from roblox_discord import VerificationClient, BloxlinkError

roblox = Client()
bloxlink = VerificationClient(roblox)


async def main():
    """
    todo: move over to a proper testing framework
    I'm not using one now because I don't care enough
    """

    user = await bloxlink.get_user(84117866944663552)  # justin
    assert user.id == 92587045
    assert user.name == "Tigerism"

    base_user = await bloxlink.get_user(84117866944663552, expand=False)
    assert base_user.id == 92587045

    try:
        await bloxlink.get_user(0)
        raise AssertionError
    except BloxlinkError:
        pass

    try:
        await bloxlink.get_user(0, expand=False)
        raise AssertionError
    except BloxlinkError:
        pass


asyncio.get_event_loop().run_until_complete(main())
