from musicdex.model.playlist import Playlist, ArtContext
from musicdex.model.channels import Channel
from musicdex.model.description import Description
from musicdex.model.discovery import Discovery, RecentSingingStream, Channels
from musicdex.model.songs import Songs
from musicdex.model.video import Video


async def assert_discovery(response: Discovery | list[Discovery]):
    async def check(resp: Discovery):
        assert isinstance(resp, Discovery)
        assert isinstance(resp.streams, list)
        assert isinstance(resp.channels, list)
        assert isinstance(resp.recommended, list)

        for r in resp.streams:
            assert isinstance(r, RecentSingingStream)
            await assert_playlist(r.playlist)
            await assert_video(r.video)

        for r in resp.channels:
            assert isinstance(r, Channels)

        for r in resp.recommended:
            await assert_playlist(r)

    if isinstance(response, list):
        for resp in response:
            await check(resp)

    if isinstance(response, Discovery):
        await check(response)


async def assert_songs(response: Songs | list[Songs]):
    async def check(resp: Songs):
        assert isinstance(resp, Songs)
        assert isinstance(resp.channel, Channel) or isinstance(resp.channel, list)

        await assert_channels(resp.channel)

    if isinstance(response, list):
        for resp in response:
            await check(resp)

    if isinstance(response, Songs):
        await check(response)


async def assert_channels(response: Channel | list[Channel]):
    if isinstance(response, list):
        for resp in response:
            assert isinstance(resp, Channel)

    if isinstance(response, Channel):
        assert isinstance(response, Channel)


async def assert_video(response: Video | list[Video]):
    async def check(resp: Video):
        assert isinstance(resp, Video)
        assert isinstance(resp.channel, Channel)

    if isinstance(response, list):
        for resp in response:
            await check(resp)

    if isinstance(response, Video):
        await check(response)


async def assert_playlist(response: Playlist | list[Playlist]):
    async def check(resp: Playlist):
        assert isinstance(resp, Playlist)
        if resp.content:
            assert isinstance(resp.content, list)
            for r in resp.content:
                assert isinstance(r, Songs)

        if resp.description is not None:
            assert (
                isinstance(resp.description, Description)
                or isinstance(resp.description, str)
                or isinstance(resp.description, dict)
            )
        if resp.art_context is not None:
            assert isinstance(resp.art_context, ArtContext)

    if isinstance(response, list):
        for resp in response:
            await check(resp)

    else:
        await check(response)
