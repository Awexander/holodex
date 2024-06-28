import pytest
from musicdex.client import MusicdexClient

from tests.test_musicdex_model import assert_playlist


@pytest.mark.asyncio
async def test_playlist_latest(musicdex: MusicdexClient):
    response = await musicdex.playlist("latest", org="Hololive")
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_artist(musicdex: MusicdexClient):
    response = await musicdex.playlist(
        category="artist", channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g"
    )
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_dailyrandom(musicdex: MusicdexClient):
    response = await musicdex.playlist(
        category="dailyrandom", channel_id="UCoSrY_IQQVpmIRZ9Xf-y93g"
    )
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_hot(musicdex: MusicdexClient):
    response = await musicdex.playlist(category="hot", org="Hololive")
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_mv(musicdex: MusicdexClient):
    response = await musicdex.playlist(category="mv", org="Hololive")
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_video(musicdex: MusicdexClient):
    response = await musicdex.playlist(category="video", video_id="YjzQm_34aVw")
    await assert_playlist(response=response)


@pytest.mark.asyncio
async def test_playlist_weekly(musicdex: MusicdexClient):
    response = await musicdex.playlist(category="weekly", org="Hololive")
    await assert_playlist(response=response)
