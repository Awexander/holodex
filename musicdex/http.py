from typing import Any, Optional, Type
from types import TracebackType
from aiohttp import ClientSession
from typing_extensions import Literal


JSONDict = dict[str, Any]


class MusicdexHttpClient:
    BASE_URL = "https://music.holodex.net/api/v2"

    def __init__(self, key: Optional[str] = None) -> None:
        self.key = key
        self.session = ClientSession()

    @property
    def headers(self) -> dict[str, Any]:
        headers: dict[str, Any] = {}
        if self.key:
            headers["X-APIKEY"] = self.key
        return headers

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

    async def get_trending(self, **params: JSONDict) -> Any:
        return await self.request("GET", f"/songs/hot", params=params)

    async def get_discovery(
        self, endpoint: Optional[str] = None, **params: JSONDict
    ) -> Any:
        return await self.request(
            "GET", f"/musicdex/discovery/{endpoint}", params=params
        )

    async def get_channels(self, **params: JSONDict) -> Any:
        return await self.request(
            "GET", f"/channels", params={"limit": 100, "offset": 0, **params}
        )

    async def get_channels_details(self, endpoint: str, **params: JSONDict) -> Any:
        return await self.request("GET", endpoint=f"/channels/{endpoint}", **params)

    async def get_playlist(self, endpoint: str, **params: JSONDict) -> Any:
        return await self.request(
            "GET", f"/musicdex/playlist/{endpoint}", params=params
        )

    async def get_radio(
        self, endpoint: Optional[str] = None, **params: JSONDict
    ) -> Any:
        return await self.request("GET", f"/musicdex/radio/{endpoint}", params=params)

    async def get_latest(self, **params: JSONDict) -> Any:
        return await self.request(
            "POST", f"/songs/latest", data={"limit": 50, "offset": 0, **params}
        )
