import asyncio
from roblox import Client
from roblox_bloxlink import BloxlinkClient

roblox = Client()
bloxlink = BloxlinkClient(roblox)


async def main():
    user = await bloxlink.get_user(84117866944663552)  # justin
    assert user.id == 92587045
    assert user.name == "Tigerism"

asyncio.get_event_loop().run_until_complete(main())
