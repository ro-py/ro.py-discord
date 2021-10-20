import asyncio
from roblox import Client
from roblox_discord import VerificationClient, BloxlinkError

roblox = Client()
verification = VerificationClient(roblox)


async def main():
    """
    todo: move over to a proper testing framework
    I'm not using one now because I don't care enough
    """

    user = await verification.get_user_bloxlink(84117866944663552)  # justin
    assert user.id == 92587045
    assert user.name == "Tigerism"

    base_user = await verification.get_user_bloxlink(84117866944663552, expand=False)
    assert base_user.id == 92587045

    try:
        await verification.get_user_bloxlink(0)
        raise AssertionError
    except BloxlinkError:
        pass

    try:
        await verification.get_user_bloxlink(0, expand=False)
        raise AssertionError
    except BloxlinkError:
        pass


asyncio.get_event_loop().run_until_complete(main())
