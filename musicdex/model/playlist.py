
from typing import Union, Optional, Any, Dict
from attrs import define

from musicdex.model.trending import Content
from musicdex.model.description import Description

JSONDict = Dict[str, Any]

@define(kw_only=True)
class ArtContext:
    channels: Optional[list[str]] = None
    videos: Optional[list[str]] = None

@define(kw_only=True)
class Playlist:
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    listed: Optional[bool] = None
    owner: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    rank: Optional[int] = None
    description: Union[JSONDict, Description, None] = None
    content: Union[list[JSONDict], list[Content], None]  = None
    art_context: Union[JSONDict, ArtContext, None] = None
    
    def __attrs_post_init__(self):
        if self.art_context and isinstance(self.art_context, Dict):
            self.art_context = ArtContext(**self.art_context)
            
        if self.content:
            self.content = [Content(**r) for r in self.content] #type: ignore

        if self.description:
            if isinstance(self.description, str):
                import json
                self.description = json.loads(self.description)
                
            if isinstance(self.description, dict):
                self.description = Description(**self.description)