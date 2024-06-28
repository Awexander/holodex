# holodex

> Holodex and Musicdex api wrapper

### Musicdex api are scraped from [music.holodex.net](https://music.holodex.net/) and not officially documented by holodex team.

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
## Example Musicdex

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
        await musicdex.radio(category="hot")
        await musicdex.radio(category='artist', channel_id=channel_id)

        # playlist
        await musicdex.playlist(category="latest", org="Hololive")
        await musicdex.playlist(category="weekly", org="Hololive")
        await musicdex.playlist(category="mv", org="Hololive", sort="random")
        await musicdex.playlist(category="dailyrandom", channel_id=channel_id)
        await musicdex.playlist(category='video', video_id=video_id)
        await musicdex.playlist(category="hot", org="Hololive")
        await musicdex.playlist(playlist_id=":hot[]")

if __name__ == "__main__":
    asyncio.run(main())
    
```
