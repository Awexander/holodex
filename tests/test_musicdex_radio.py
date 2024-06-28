import pytest
from musicdex.client import MusicdexClient

from tests.test_musicdex_model import assert_playlist


@pytest.mark.asyncio
async def test_radio_channel(musicdex: MusicdexClient):
    response = await musicdex.radio(
        category="artist", channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g"
    )
    await assert_playlist(response)


@pytest.mark.asyncio
async def test_radio_hot(musicdex: MusicdexClient):
    response = await musicdex.radio(category="hot")
    await assert_playlist(response)
