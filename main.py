
import asyncio
from musicdex.client import MusicdexClient
import dotenv

from typing import Union, List, Any
from musicdex.model.channels import Channel
from musicdex.model.discovery import Discovery
from musicdex.model.description import Description
from musicdex.model.playlist import Playlist
from musicdex.model.trending import Content
from musicdex.model.video import Video


async def main():
    APIKEY = dotenv.dotenv_values().get('APIKEY')
    channel_id = 'UCoSrY_IQQVpmIRZ9Xf-y93g'
    video_id = 'uIloWxQ3Rpo'

    async with MusicdexClient(key=APIKEY) as musicdex:
        # channels
        print_result(await musicdex.channels(org="Hololive"))
        print_result(await musicdex.channels(channel_id=channel_id))

        # discovery endpoint
        print_result(await musicdex.discovery(category="channel", channel_id=channel_id))
        print_result(await musicdex.discovery(category="org", org="Hololive"))

        return
        # trending endpoint
        print_result(await musicdex.hot())
        print_result(await musicdex.hot(org="Hololive"))
        print_result(await musicdex.hot(channel_id=channel_id))

        # radio endpoint
        print_result(await musicdex.radio(category="hot"))
        print_result(await musicdex.radio(category='artist', channel_id=channel_id))

        # playlist
        print_result(await musicdex.playlist(category="weekly", org="Hololive"))
        print_result(await musicdex.playlist(category="latest", org="Hololive"))
        print_result(await musicdex.playlist(category="mv", org="Hololive", sort="random"))
        print_result(await musicdex.playlist(category="dailyrandom", channel_id=channel_id))
        print_result(await musicdex.playlist(category='video', video_id=video_id))
        print_result(await musicdex.playlist(playlist_id=":weekly[org=Hololive]"))


def print_result(
        response: Union[
            Channel,
            Discovery,
            Description,
            Playlist,
            Content,
            Video,
            List[Any],
            None
        ]) -> None:

    if isinstance(response, Channel):
        print(f"Channel : {response.id}")
    if isinstance(response, Discovery):
        print(f"Discovery : {response.streams[0].video}")
        print(f"Discovery : {response.streams[0].playlist}")
        print(f"Discovery : {response.channels[0].id}")
        print(f"Discovery : {response.recommended[0].id}")
    if isinstance(response, Description):
        print(f"Description : {response.id}")
    if isinstance(response, Playlist):
        print(f"Playlist : {response.id}")
    if isinstance(response, Content):
        print(f"Content : {response.id}")
    if isinstance(response, Video):
        print(f"Video : {response.id}")

    if isinstance(response, List):
        resp: Any = response[0]
        if isinstance(resp, Channel):
            print(f"Channel : {resp.id}")
        if isinstance(resp, Discovery):
            print(f"Discovery : {resp.streams[0].video}")
            print(f"Discovery : {resp.streams[0].playlist}")
            print(f"Discovery : {resp.channels[0].id}")
            print(f"Discovery : {resp.recommended[0].id}")
        if isinstance(resp, Description):
            print(f"Description : {resp.id}")
        if isinstance(resp, Playlist):
            print(f"Playlist : {resp.id}")
        if isinstance(resp, Content):
            print(f"Content : {resp.id}")
        if isinstance(resp, Video):
            print(f"Video : {resp.id}")


if __name__ == "__main__":
    asyncio.run(main())
