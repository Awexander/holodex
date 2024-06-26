
from typing import Optional, Union, Any, Dict
from attrs import define
from musicdex.model.channels import Channel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class Video:
    id: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    topic_id: Optional[str] = None
    published_at: Optional[str] = None
    available_at: Optional[str] = None
    duration: Optional[int] = None
    status: Optional[str] = None
    songcount: Optional[str] = None
    channel: Union[JSONDict, Channel, None] = None

    def __attrs_post_init__(self):
        if self.channel and isinstance(self.channel, Dict):
            self.channel = Channel(**self.channel)
