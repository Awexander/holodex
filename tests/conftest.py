import pytest_asyncio
from collections.abc import AsyncGenerator
from dotenv import dotenv_values
from holodex.client import HolodexClient
from musicdex.client import MusicdexClient


@pytest_asyncio.fixture()
async def holodex() -> AsyncGenerator[HolodexClient, None]:
    APIKEY = dotenv_values().get("APIKEY")
    client = HolodexClient(key=APIKEY)
    print(client)
    yield client
    if client.session:
        await client.session.close()


@pytest_asyncio.fixture()
async def musicdex() -> AsyncGenerator[MusicdexClient, None]:
    APIKEY = dotenv_values().get("APIKEY")
    client = MusicdexClient(key=APIKEY)
    yield client
    if client.session:
        await client.close()
