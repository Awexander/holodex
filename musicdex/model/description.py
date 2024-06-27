

from typing import Union, Optional, Any, Dict
from attrs import define, field

from musicdex.model.channels import Channel
from musicdex.model.base import BaseModel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class Description(BaseModel):
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
    __mentions: Any = field(default=None, init=False, repr=False)
    __channel: Any = field(default=None, init=False, repr=False)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__mentions: Any = kwargs.get('mentions')
        self.__channel: Any = kwargs.get('channel')

        if self.__channel:
            self.channel = Channel(**self.__channel)

        if self.__mentions:
            self.mentions = [Channel(**r) for r in self.__mentions]
