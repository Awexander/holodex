import pytest
from dotenv import dotenv_values
from holodex.client import HolodexClient

@pytest.fixture()
async def client():
    APIKEY = dotenv_values().get('APIKEY')
    client = HolodexClient(key=APIKEY)
    yield client
    if client.session:
        await client.session.close()
