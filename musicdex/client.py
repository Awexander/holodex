
from typing import Any, Optional

from aiohttp.client import ClientSession
from typing_extensions import Literal

from musicdex.model.trending import Content
from musicdex.model.discovery import Discovery
from musicdex.model.channels import Channel
from musicdex.model.discovery import Playlist

from musicdex.http import MusicdexHttpClient

class MusicdexClient(MusicdexHttpClient):
    def __init__(
        self, key: Optional[str] = None, session: Optional[ClientSession] = None
    ) -> None:
        super().__init__(key=key, session=session)
        
    def __get_params(
        self, keys: dict[str, Any], exclude: Optional[list[str]] = None
    ) -> dict[str, Any]:
        keys.pop("self")
        if exclude:
            for key in exclude:
                keys.pop(key)
        return {k: v for k, v in keys.items() if v is not None}

    async def trending(self, org: str) -> list[Content]:
        return [Content(**r) for r in await self.get_trending(org)]
    
    async def discovery(self, org: str) -> Discovery:
        return Discovery(**await self.get_discovery(org))
    
    async def channels(self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        type: Optional[Literal["vtuber"]] = None,
        order: Optional[Literal["asc", "desc"]] = None,
        org: Optional[
            Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]
        ] = None,
        sort: Optional[str] = None
    ) -> list[Channel]:
        params = self.__get_params(locals())
        return [Channel(**r) for r in await self.get_channels(**params)]
    
    async def playlist(self, id: str) -> Playlist:
        return Playlist(**await self.get_playlist(id=id))
    
    async def radio(self,
        *, 
        type: Optional[str] = None, 
        org: Optional[
            Literal["All Vtubers", "Hololive", "Nijisanji", "Independents"]
        ] = None,
    ) -> Any:
        params = self.__get_params(locals())
        return params