# ro.py-discord
Small library to connect Discord with ro.py via Bloxlink and RoVer.

```py
import asyncio
from roblox import Client
from roblox_discord import VerificationClient, BloxlinkError

roblox = Client()
bloxlink = VerificationClient(roblox)


async def main():
    user = await bloxlink.get_user(84117866944663552)  # justin
    print("Name:", user.name)
    print("Status:", await user.get_status())


asyncio.get_event_loop().run_until_complete(main())
```
