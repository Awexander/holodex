
import asyncio
from musicdex.client import MusicdexClient
import dotenv


async def main():
    APIKEY = dotenv.dotenv_values().get('APIKEY')
    channel_id = 'UCoSrY_IQQVpmIRZ9Xf-y93g'
    video_id = 'uIloWxQ3Rpo'

    async with MusicdexClient(key=APIKEY) as musicdex:
        # latest songs
        await musicdex.latest(org="Hololive", limit=20)
        
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