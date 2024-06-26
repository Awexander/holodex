from types import TracebackType
from typing import Any, Optional, Type

from aiohttp import ClientSession
from typing_extensions import Literal

JSONDict = dict[str, Any]

class MusicdexHttpClient:
    BASE_URL = "https://music.holodex.net/api/v2"

    def __init__(
        self, key: Optional[str] = None, session: Optional[ClientSession] = None
    ) -> None:
        self.session = session
        self.key = key

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def __aenter__(self) -> "MusicdexHttpClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        await self.close()

    @property
    def headers(self) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        if self.key:
            headers["X-APIKEY"] = self.key
        return headers

    async def request(
        self,
        method: Literal["GET", "POST"],
        endpoint: str,
        **kwargs: Any,
    ) -> Any:
        if not self.session:
            self.session = ClientSession()

        async with self.session.request(
            method,
            self.BASE_URL + endpoint,
            headers=self.headers,
            **kwargs,
        ) as r:
            return await r.json()

    async def get_trending(self, org: str = "Hololive") -> Any:
        return await self.request("GET", f"/songs/hot?org={org}")

    async def get_discovery(self, org: str = "Hololive", **params: Any) -> Any:
        return await self.request("GET", f"/musicdex/discovery/org/{org}", params=params)
    
    async def get_channels(self, **params: Any) -> Any:
        return await self.request(
            "GET", f"/channels", params={"limit": 100, "offset": 0, **params}
        )
    
    async def get_playlist(self, id: str) -> Any:
        return await self.request("GET", F"/musicdex/playlist/{id}")
    
    async def get_radio(self, **params: JSONDict) -> Any:
        return await self.get_discovery(params=params)
