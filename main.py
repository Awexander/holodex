
import asyncio
from musicdex.client import MusicdexClient
url = 'https://www.youtube.com/watch?v=uIloWxQ3Rpo'
async def main():
    client = MusicdexClient(key='a14ca036-6868-4592-9532-1fc15dab64d0')
    trending = await client.trending(org="Hololive")
    for trends in trending:
        print(trends)

if __name__ == "__main__":
    asyncio.run(main())