import asyncio
from roblox import Client
from roblox_bloxlink import BloxlinkClient

roblox = Client()
bloxlink = BloxlinkClient(roblox)


async def main():
    user = await bloxlink.get_user(1)

asyncio.get_event_loop().run_until_complete(main())
