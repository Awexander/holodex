from typing import Optional, Any, Dict
from attrs import define, field

from musicdex.model.base import BaseModel
from musicdex.model.channels import Channel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class Songs(BaseModel):
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
    channel: Optional[Channel] = None
    __channel: Any = field(default=None, init=False, repr=False)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__channel: Any = kwargs.get("channel")
        if self.__channel:
            self.channel = Channel(**self.__channel)
