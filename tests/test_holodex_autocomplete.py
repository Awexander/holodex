import pytest
from holodex.client import HolodexClient


@pytest.mark.asyncio
async def test_autocomplete(holodex: HolodexClient):
    assert isinstance(holodex, HolodexClient)
    channel = await holodex.autocomplete("gawr gura ch")
    assert channel.contents[0].text == "Gawr Gura Ch. hololive-EN"
