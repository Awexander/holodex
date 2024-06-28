from typing import Optional, Union, Any, Dict
from attrs import define, field

from musicdex.model.playlist import Playlist
from musicdex.model.video import Video
from musicdex.model.base import BaseModel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class RecentSingingStream:
    __video: Any = field(default=None, init=False, repr=False)
    __playlist: Any = field(default=None, init=False, repr=False)

    def __init__(
        self,
        video: Union[JSONDict, Video, None] = None,
        playlist: Union[JSONDict, Playlist, None] = None,
        **kwargs: Any,
    ) -> None:
        self.__video = video
        self.__playlist = playlist

    def __repr__(self) -> str:
        return f"RecentSingingStream({self.video},{self.playlist})"

    @property
    def video(self) -> Video:
        if self.__video:
            return Video(**self.__video)

        return Video()

    @property
    def playlist(self) -> Playlist:
        if self.__playlist:
            return Playlist(**self.__playlist)

        return Playlist()


@define(kw_only=True)
class Channels(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    english_name: Optional[str] = None
    song_count: Optional[str] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


@define(kw_only=True)
class Discovery:
    __streams: Any = field(default=None, init=False, repr=False)
    __channels: Any = field(default=None, init=False, repr=False)
    __recommended: Any = field(default=None, init=False, repr=False)

    def __init__(
        self,
        *,
        recentSingingStreams: JSONDict,
        channels: JSONDict,
        recommended: JSONDict,
        **kwargs: Any,
    ) -> None:
        self.__streams = recentSingingStreams
        self.__channels = channels
        self.__recommended = recommended

    def __repr__(self) -> str:
        return f"Discovery({self.streams},{self.channels},{self.recommended})"

    @property
    def streams(self) -> list[RecentSingingStream]:
        return [RecentSingingStream(**r) for r in self.__streams]

    @property
    def channels(self) -> list[Channels]:
        return [Channels(**r) for r in self.__channels]

    @property
    def recommended(self) -> list[Playlist]:
        return [Playlist(**r) for r in self.__recommended.get("playlists")]
