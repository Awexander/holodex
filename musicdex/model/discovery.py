
from typing import Optional, Union, Any, Dict
from attrs import define, field

from musicdex.model.playlist import Playlist
from musicdex.model.video import Video

JSONDict = Dict[str, Any]

@define(kw_only=True)
class RecentSingingStream:
    video: Union[JSONDict, Video, None] = None
    playlist: Union[JSONDict, Playlist, None] = None
    
    def __attrs_post_init__(self):
        if self.video and isinstance(self.video, dict):
            self.video = Video(**self.video)
        
        if self.playlist and isinstance(self.playlist, dict):
            self.playlist = Playlist(**self.playlist)
        
@define(kw_only=True)
class Channels:
    id: Optional[str] = None
    name: Optional[str] = None
    english_name: Optional[str] = None
    song_count: Optional[str] = None

@define(kw_only=True)
class Discovery:
    __streams: Any = field(default=None, init=False, repr=False)
    __channels: Any = field(default=None, init=False, repr=False)
    __recommended: Any = field(default=None, init=False, repr=False)
    
    def __init__(self, 
        *, 
        recentSingingStreams: JSONDict, 
        channels : JSONDict,
        recommended : JSONDict,
        **kwargs #type: ignore
    ) -> None:
        self.__streams = recentSingingStreams
        self.__channels = channels
        self.__recommended = recommended
    
    def __repr__(self) -> str:
        return F"Discovery({self.streams},{self.channels},{self.recommended})"
    
    @property
    def streams(self) -> list[RecentSingingStream]:
        return [RecentSingingStream(**r) for r in self.__streams]
    
    @property
    def channels(self) -> list[Channels]:
        return [Channels(**r) for r in self.__channels]
    
    @property
    def recommended(self) -> list[Playlist]:
        return [Playlist(**r) for r in self.__recommended.get('playlists')]
    