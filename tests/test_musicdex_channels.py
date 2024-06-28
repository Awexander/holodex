import pytest
from musicdex.client import MusicdexClient

from tests.test_musicdex_model import assert_channels

@pytest.mark.asyncio
async def test_channels_org(musicdex: MusicdexClient):
    response = await musicdex.channels(org="Hololive")
    await assert_channels(response)
    
@pytest.mark.asyncio
async def test_channels_channel(musicdex: MusicdexClient):
    response = await musicdex.channels(channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g")
    await assert_channels(response)