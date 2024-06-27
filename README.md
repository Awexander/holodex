# holodex

[![PyPI version](https://badge.fury.io/py/holodex.svg)](https://badge.fury.io/py/holodex)
[![PyPI downloads](https://img.shields.io/pypi/dm/holodex.svg)](https://pypi.python.org/pypi/holodex)
[![CodeFactor](https://www.codefactor.io/repository/github/ombe1229/holodex/badge)](https://www.codefactor.io/repository/github/ombe1229/holodex)
[![Github release](https://github.com/ombe1229/holodex/actions/workflows/ci.yml/badge.svg)](https://github.com/ombe1229/holodex/actions/workflows/ci.yml)

> Holodex and Musicdex api wrapper

## Example Holodex

```py
import asyncio
from holodex.client import HolodexClient


async def main():
    async with HolodexClient() as client:
        search = await client.autocomplete("iofi")
        channel_id = search.contents[0].value
        print(channel_id)

        channel = await client.channel(channel_id)
        print(channel.name)
        print(channel.subscriber_count)

        videos = await client.videos_from_channel(channel_id, "videos")
        print(videos.contents[0].title)

        channels = await client.channels(limit=100)

        print(channels[0].name)
        print(channels[0].subscriber_count)


asyncio.run(main())


"""
UCAoy6rzhSf4ydcYjJw3WoVg
Airani Iofifteen Channel hololive-ID
508000
Freetalk dan Terima Kasih Superchat! + Risu OG Song React?!
Nanashi Mumei Ch. hololive-EN
528000
"""

```
## Example Holodex

```py
import asyncio
from musicdex.client import MusicdexClient
import dotenv


async def main():
    APIKEY = dotenv.dotenv_values().get('APIKEY')
    channel_id = 'UCoSrY_IQQVpmIRZ9Xf-y93g'
    video_id = 'uIloWxQ3Rpo'

    async with MusicdexClient(key=APIKEY) as musicdex:
        # channels
        await musicdex.channels(org="Hololive")
        await musicdex.channels(channel_id=channel_id)

        # discovery endpoint
        await musicdex.discovery(category="channel", channel_id=channel_id)
        await musicdex.discovery(category="org", org="Hololive")

        # trending endpoint
        await musicdex.hot()
        await musicdex.hot(org="Hololive")
        await musicdex.hot(channel_id=channel_id)

        # radio endpoint
        await musicdex.radio(type="hot")
        await musicdex.radio(type='artist', channel_id=channel_id)

        # playlist
        await musicdex.playlist(type="weekly", org="Hololive")
        await musicdex.playlist(type="latest", org="Hololive")
        await musicdex.playlist(type="mv", org="Hololive", sort="random")
        await musicdex.playlist(type="dailyrandom", channel_id=channel_id)
        await musicdex.playlist(type='video', video_id=video_id)
        await musicdex.playlist(playlist_id="")

if __name__ == "__main__":
    asyncio.run(main())
    
```

## Installation

```
python -m pip install holodex
```
