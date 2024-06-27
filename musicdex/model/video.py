
from typing import Optional, Union, Any, Dict
from attrs import define

from musicdex.model.channels import Channel
from musicdex.model.base import BaseModel

JSONDict = Dict[str, Any]

@define(kw_only=True)
class Video(BaseModel):
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

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        
    def __attrs_post_init__(self):
        if self.channel and isinstance(self.channel, Dict):
            self.channel = Channel(**self.channel)
