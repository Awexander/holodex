

from musicdex.model.base import BaseModel

from typing import Any, Dict, Optional, Union
from attrs import define

JSONDict = Dict[str, Any]

@define(kw_only=True)
class Hot(BaseModel):
    a: Optional[str] = None
    b: Optional[int] = None
    c: Union[str, int, None] = None
    d: Optional[JSONDict] = None
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)