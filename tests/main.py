import asyncio
from roblox import Client
from roblox_discord import VerificationClient, BloxlinkError, RoVerError

roblox = Client()
verification = VerificationClient(roblox)


async def main():
    """
    todo: move over to a proper testing framework
    I'm not using one now because I don't care enough
    """

    # Bloxlink
    user = await verification.get_user_bloxlink(84117866944663552)  # justin
    assert user.id == 92587045

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

    # RoVer
    user = await verification.get_user_rover(113691352327389188)  # evaera
    print(user.id)
    assert user.id == 92658764

    partial_user = await verification.get_user_rover(113691352327389188, expand=False)
    assert partial_user.id == 92658764

    try:
        await verification.get_user_rover(0)
        raise AssertionError
    except RoVerError:
        pass

    try:
        await verification.get_user_rover(0, expand=False)
        raise AssertionError
    except RoVerError:
        pass

    # Both
    user = await verification.get_user(197683356643753984)
    assert user.id == 968108160

    partial_user = await verification.get_user(197683356643753984, expand=False)
    assert partial_user.id == 968108160


asyncio.get_event_loop().run_until_complete(main())
