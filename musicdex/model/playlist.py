
from typing import Union, Optional, Any, Dict
from attrs import define, field

from musicdex.model.trending import Content
from musicdex.model.description import Description
from musicdex.model.base import BaseModel

JSONDict = Dict[str, Any]


@define(kw_only=True)
class ArtContext(BaseModel):
    channels: Optional[list[str]] = None
    videos: Optional[list[str]] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


@define(kw_only=True)
class Playlist(BaseModel):
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    listed: Optional[bool] = None
    owner: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    rank: Optional[int] = None
    description: Union[JSONDict, Description, str, None] = None
    content: Union[list[Content], None] = None
    art_context: Union[ArtContext, None] = None
    __content: Any = field(default=None, init=False, repr=False)
    __description: Any = field(default=None, init=False, repr=False)
    __art_context: Any = field(default=None, init=False, repr=False)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.__description: Any = kwargs.get('description')
        self.__content: Any = kwargs.get('content')
        self.__art_context: Any = kwargs.get('art_context')

        if self.__content:
            self.content = [Content(**r) for r in self.__content]

        if self.__art_context:
            self.art_context = ArtContext(**self.__art_context)

        if self.__description:
            import json
            try:
                self.description = json.loads(self.__description)
            except json.JSONDecodeError:
                self.description = self.__description
                return

            # self.description = Description(
            #     **self.description)  # type: ignore
