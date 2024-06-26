
from typing import Any, Optional, Type
from types import TracebackType

from typing_extensions import Literal

from musicdex.model.trending import Content
from musicdex.model.discovery import Discovery
from musicdex.model.channels import Channel
from musicdex.model.discovery import Playlist

from musicdex.http import MusicdexHttpClient
from musicdex.errno import *


class MusicdexClient:
    def __init__(self, key: Optional[str] = None) -> None:
        self.session = MusicdexHttpClient(key=key)

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
        exclude: Optional[list[str]] = None
    ) -> str:
        keys.pop("self")
        cat = keys.get('type')

        if exclude:
            for key in exclude:
                keys.pop(key)

        if keys.get('type'):
            keys.pop('type')

        params = [f"{k}={v}" for k, v in keys.items() if v is not None]
        return f":{cat}[" + ",".join(params) + "]"

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

    async def hot(
        self,
        *,
        channel_id: Optional[str] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> list[Content]:
        params = self.__get_body_params(locals())
        if channel_id and org:
            raise MusicdexParamError("Either `channel_id` or `org` only.")

        return [Content(**r) for r in await self.session.get_trending(**params)]

    async def discovery(
        self,
        category: Literal["channel", "org"],
        *,
        ch: Optional[str] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> Discovery:
        params = self.__get_body_params(
            locals(), exclude=["category", "ch", "org"])
        endpoint = {"channel": f"channel/{ch}", "org": f'org/{org}'}

        if category == "channel" and not ch:
            raise MusicdexParamError("`ch` is undefined.")

        if category == 'org' and not org:
            raise MusicdexParamError("`org` is undefined.")

        return Discovery(**await self.session.get_discovery(endpoint=endpoint.get(category), **params))

    async def channels(
        self,
        *,
        channel_id: Optional[str] = None,
        offset: Optional[int] = None,
        type: Optional[Literal["vtuber"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        limit: Optional[int] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
        sort: Optional[Literal["latest", "random", "suborg"]] = None,
    ) -> list[Channel]:
        params = self.__get_body_params(locals(), exclude=["channel_id"])
        if channel_id:
            endpoint = f'/{channel_id}'  # TODO : add channel details endpoint

        return [Channel(**r) for r in await self.session.get_channels(**params)]

    async def playlist(
        self,
        type: Optional[
            Literal["mv", "dailyrandom",
                    "weekly", "video", "latest"]] = None,
        *,
        id: Optional[str] = None,
        ch: Optional[str] = None,
        sort: Optional[Literal["latest", "random"]] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive",
                    "Nijisanji", "Independents"]
        ] = None,
    ) -> Playlist:
        params = self.__get_path_params(locals(), exclude=["type"])
        if type in ('weekly', 'mv', 'latest') and not org:
            raise MusicdexParamError("`org` is undefined.")

        if type == 'dailyrandom' and not ch:
            raise MusicdexParamError("`ch` is undefined.")

        if type == 'video' and not id:
            raise MusicdexParamError("`id` is undefined.")

        return Playlist(**await self.session.get_playlist(endpoint=params))

    async def radio(
        self,
        type: Literal["artist"],
        ch: str,
    ) -> Any:
        params = self.__get_path_params(locals(), exclude=["type"])
        if not ch and not not type:
            raise MusicdexParamError("`type` and `ch` is undefined.")

        return Playlist(**await self.session.get_radio(endpoint=params))
