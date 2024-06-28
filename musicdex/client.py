
from typing import Any, Optional, Type, overload
from types import TracebackType

from typing_extensions import Literal

from musicdex.model.songs import Songs
from musicdex.model.discovery import Discovery
from musicdex.model.channels import Channel
from musicdex.model.discovery import Playlist

from musicdex.http import MusicdexHttpClient
from musicdex.errno import *


class MusicdexClient:
    def __init__(self, key: Optional[str] = None) -> None:
        self.session = MusicdexHttpClient(key=key)

    @overload
    async def hot(
        self,
        *,
        org: Literal["All Vtubers", "Hololive",
                     "Nijisanji", "Independents"]
    ) -> list[Songs]:
        ...

    @overload
    async def hot(
        self,
        *,
        channel_id: str
    ) -> list[Songs]:
        ...

    @overload 
    async def latest(
        self,
        *,
        org: Literal[
            "All Vtubers", "Hololive",
            "Nijisanji", "Independents"
        ],
        limit: Optional[int] = 50,
        offset: Optional[int] = 0,
    ) -> list[Songs]:
        ...
    
    @overload
    async def latest(
        self, 
        *,
        channel_id: str,
        limit: Optional[int] = 50,
        offset: Optional[int] = 0,
    ) -> list[Songs]:
        ...
        
    @overload
    async def hot(self) -> list[Songs]:
        ...

    @overload
    async def discovery(
        self,
        category: Literal["channel"],
        *,
        channel_id: str,
    ) -> Discovery:
        ...

    @overload
    async def discovery(
        self,
        category: Literal['org'],
        *,
        org: Literal["All Vtubers", "Hololive",
                     "Nijisanji", "Independents"],
    ) -> Discovery:
        ...

    @overload
    async def channels(
        self,
        *,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ],
        offset: Optional[str] = None,
        limit: Optional[int] = None,
        type: Optional[Literal["vtuber"]] = None,
        sort: Optional[Literal["latest", "random", "suborg"]] = None,
    ) -> list[Channel]:
        ...

    @overload
    async def channels(
        self,
        channel_id: str
    ) -> list[Channel]:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["mv"],
        *,
        org: Literal["All Vtubers", "Hololive",
                     "Nijisanji", "Independents"],
        sort: Optional[Literal["random", "latest"]] = None
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["dailyrandom"],
        *,
        channel_id: str
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["weekly"],
        *,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ]
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["video"],
        *,
        video_id: str
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["latest"],
        *,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ]
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["hot"],
        *,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ]
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        category: Literal["artist"],
        *,
        channel_id: str
    ) -> Playlist:
        ...

    @overload
    async def playlist(
        self,
        *,
        playlist_id: str
    ) -> Playlist:
        ...

    async def hot(
        self,
        *,
        channel_id: Optional[str] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> list[Songs]:
        if channel_id and org:
            raise ValueError("Either `channel_id` or `org` only.")

        # if not channel_id and not org:
        #     return await self.radio(category="hot")

        params = self.__get_body_params(locals())
        return [Songs(**r) for r in await self.session.get_trending(**params)]

    async def discovery(
        self,
        category: Literal["channel", "org"],
        *,
        channel_id: Optional[str] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> Discovery:
        endpoint = {"channel": f"channel/{channel_id}", "org": f'org/{org}'}

        if category == "channel" and not channel_id:
            raise ValueError("`channel_id` is undefined.")

        if category == 'org' and not org:
            raise ValueError("`org` is undefined.")

        params = self.__get_body_params(
            locals(), exclude=["category", "channel_id", "org", 'endpoint'])
        return Discovery(**await self.session.get_discovery(endpoint=endpoint.get(category), **params))

    async def channels(  # type: ignore
        self,
        *,
        channel_id: Optional[str] = None,
        offset: Optional[int] = None,
        type: Optional[Literal["vtuber"]] = None,
        limit: Optional[int] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
        sort: Optional[Literal["latest", "random", "suborg"]] = None,
    ) -> list[Channel] | Channel:
        params = self.__get_body_params(locals(), exclude=["channel_id"])
        if channel_id:
            return Channel(**await self.session.get_channels_details(channel_id))

        return [Channel(**r) for r in await self.session.get_channels(**params)]

    async def playlist(
        self,
        category: Optional[
            Literal["mv", "dailyrandom",
                    "weekly", "video", "latest",
                    "hot", "artist"]
        ] = None,
        *,
        playlist_id: Optional[str] = None,
        video_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        sort: Optional[Literal["latest", "random"]] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> Playlist:
        if playlist_id is not None:
            params = playlist_id

        else:
            if category in ('weekly', 'mv', 'latest', 'hot') and not org:
                raise ValueError("`org` is undefined.")

            if category == 'dailyrandom' and not channel_id:
                raise ValueError("`ch` is undefined.")

            if category == 'video' and not video_id:
                raise ValueError("`video_id` is undefined.")

            if category == 'artist' and not channel_id:
                raise ValueError("`channel_id` is undefined.")

            params = self.__get_path_params(
                locals(), exclude=["category"],
                change=['channel_id', 'video_id']
            )

        return Playlist(**await self.session.get_playlist(endpoint=params))

    async def radio(
        self,
        category: Optional[Literal["artist", "hot"]] = None,
        *,
        channel_id: Optional[str] = None,
    ) -> Playlist:
        if category == "artist" and not channel_id:
            raise ValueError("`channel_id` is undefined.")

        endpoint = self.__get_path_params(
            locals(), exclude=["category"],
            change=['channel_id']
        )

        return Playlist(**await self.session.get_radio(endpoint=endpoint))

    async def latest(
        self, 
        *,
        channel_id: Optional[str] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
        limit: Optional[int] = 50,
        offset: Optional[int] = 0
    ) -> list[Songs]:
        excludes = ["channel_id", "org"]
        if channel_id:
            excludes = ["org"]
        
        if org:
            excludes = ["channel_id"]
            
        params = self.__get_body_params(locals(), exclude=excludes)
        return [Songs(**r) for r in await self.session.get_latest(**params)]
    
    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def __aenter__(self) -> "MusicdexClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    def __get_body_params(
        self, keys: dict[str, Any],
        exclude: Optional[list[str]] = None
    ) -> dict[str, Any]:
        keys.pop("self")
        if exclude:
            for key in exclude:
                keys.pop(key)
        return {k: v for k, v in keys.items() if v is not None}

    def __get_path_params(
        self, keys: dict[str, Any],
        exclude: Optional[list[str]] = None,
        change: Optional[list[str]] = None
    ) -> str:
        keys.pop("self")
        category = keys.get('category')  # category name
        # params to change keys name
        name_scheme = {
            "channel_id": "ch",
            "video_id": "id"
        }

        if change:
            for k in change:
                # Use list(params.keys()) to avoid "RuntimeError: dictionary keys changed during iteration"
                if k not in list(name_scheme.keys()):
                    continue

                n = name_scheme.get(k)
                if not n:
                    continue

                keys.update({n: keys.get(k)})
                keys.pop(k)  # Remove the old key key from keys

        if exclude:
            for key in exclude:
                keys.pop(key)

        field = [f"{k}={v}" for k, v in keys.items() if v is not None]
        return f":{category}[" + ",".join(field) + "]"
