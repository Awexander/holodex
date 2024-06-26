
import asyncio
from musicdex.client import MusicdexClient
import dotenv

url = 'https://www.youtube.com/watch?v=uIloWxQ3Rpo'


async def main():
    APIKEY = dotenv.dotenv_values().get('APIKEY')
    gura_channel_id = 'UCoSrY_IQQVpmIRZ9Xf-y93g'

    async with MusicdexClient(key=APIKEY) as musicdex:
        # channel = await musicdex.channels(org="Hololive")

        # discovery = await musicdex.discovery(category="channel", ch=gura_channel_id)
        # discovery = await musicdex.discovery(category="org", org="Hololive")

        trending = await musicdex.hot(org="Hololive")
        trending = await musicdex.hot(channel_id=gura_channel_id)
        print(trending)

if __name__ == "__main__":
    asyncio.run(main())
