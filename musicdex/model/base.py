
from typing import Any
from attrs import define, fields

@define(kw_only=True)
class BaseModel:
    def __init__(self, **kwargs: Any) -> None:
        # get class attributes name
        class_field = [f.name for f in fields(self.__class__)]
        
        # get only valid keyword attributes
        valid_field = {k:v for k, v in kwargs.items() if k in class_field}
        
        # set default attributes value
        for f in fields(self.__class__):
            setattr(self, f.name, f.default)
        
        # update attributes value
        for key, value in valid_field.items():
            setattr(self, key, value)
    