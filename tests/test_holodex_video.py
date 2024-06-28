import pytest
from holodex.client import HolodexClient

@pytest.mark.asyncio
async def test_video_info(holodex: HolodexClient):
    video = await holodex.video("fLAcgHX160k")
    assert video.title == "The Advent of Omegaα"
