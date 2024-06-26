

from typing import Union, Optional, Any, Dict
from attrs import define

from musicdex.model.channels import Channel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class Description:
    id: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    topic_id: Optional[str] = None
    org: Optional[str] = None
    suborg: Optional[str] = None
    published_at: Optional[str] = None
    available_at: Optional[str] = None
    duration: Optional[int] = None
    status: Optional[str] = None
    songcount: Optional[int] = None
    mentions: Union[list[JSONDict], list[Channel], None] = None
    channel: Union[JSONDict, Channel, None] = None

    def __attrs_post_init__(self):
        if self.mentions:
            self.mentions = [Channel(**r)  # type: ignore
                             for r in self.mentions]

        if self.channel and isinstance(self.channel, dict):
            self.channel = Channel(**self.channel)
