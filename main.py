
import asyncio
from musicdex.client import MusicdexClient
import dotenv

url = 'https://www.youtube.com/watch?v=uIloWxQ3Rpo'

async def main():
    APIKEY = dotenv.dotenv_values().get('APIKEY')
    gura_channel_id = 'UCoSrY_IQQVpmIRZ9Xf-y93g'
    
    async with MusicdexClient(key=APIKEY) as musicdex:
        # channels
        await musicdex.channels(org="Hololive")

        # discovery endpoint
        await musicdex.discovery(category="channel", ch=gura_channel_id)
        await musicdex.discovery(category="org", org="Hololive")

        # trending endpoint
        await musicdex.hot(org="Hololive")
        await musicdex.hot(channel_id=gura_channel_id)

        # radio endpoint
        await musicdex.radio('artist', ch=gura_channel_id)
        
        # raised error test
        await musicdex.playlist(type="mv")

if __name__ == "__main__":
    asyncio.run(main())
