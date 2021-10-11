# ro.py-bloxlink
Small library to connect bloxlink and ro.py.
```py
import asyncio
from roblox import Client
from roblox_bloxlink import BloxlinkClient, BloxlinkError

roblox = Client()
bloxlink = BloxlinkClient(roblox)


async def main():
    user = await bloxlink.get_user(84117866944663552)  # justin
    print("Name:", user.name)
    print("Status:", await user.get_status())

asyncio.get_event_loop().run_until_complete(main())
```
