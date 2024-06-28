import pytest
from musicdex.client import MusicdexClient

from tests.test_musicdex_model import assert_discovery


@pytest.mark.asyncio
async def test_discovery_org(musicdex: MusicdexClient):
    response = await musicdex.discovery(category="org", org="Hololive")
    await assert_discovery(response)


@pytest.mark.asyncio
async def test_discovery_channel(musicdex: MusicdexClient):
    response = await musicdex.discovery(
        category="channel", channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g"
    )
    await assert_discovery(response)
