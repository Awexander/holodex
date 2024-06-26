from typing import Optional, Union, Any, Dict
from attrs import define

JSONDict = Dict[str, Any]


@define(kw_only=True)
class Channel:
    name: Optional[str] = None
    english_name: Optional[str] = None


@define(kw_only=True)
class Content:
    score: Optional[int] = None
    id: Optional[str] = None
    channel_id: Optional[str] = None
    video_id: Optional[str] = None
    name: Optional[str] = None
    start: Optional[int] = None
    end: Optional[int] = None
    itunesid: Optional[int] = None
    creator_id: Optional[int] = None
    approver_id: Optional[int] = None
    art: Optional[str] = None
    amUrl: Optional[str] = None
    available_at: Optional[str] = None
    original_artist: Optional[str] = None
    status: Optional[bool] = None
    is_mv: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    channel: Union[JSONDict, Channel, None] = None

    def __attrs_post_init__(self):
        if self.channel and isinstance(self.channel, Dict):
            self.channel = Channel(**self.channel)
