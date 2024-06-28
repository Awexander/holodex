import pytest
from musicdex.client import MusicdexClient

from tests.test_musicdex_model import assert_songs


@pytest.mark.asyncio
async def test_trending_org(musicdex: MusicdexClient):
    response = await musicdex.hot(org="Hololive")
    await assert_songs(response)


@pytest.mark.asyncio
async def test_trending_channel(musicdex: MusicdexClient):
    response = await musicdex.hot(channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g")
    await assert_songs(response)


@pytest.mark.asyncio
async def test_trending_hot(musicdex: MusicdexClient):
    response = await musicdex.hot()
    await assert_songs(response)
