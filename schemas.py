from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar



class UserCreate(BaseModel):
    username: str
    password: str




























#class UserCreate(UserBase):
# pass

#class User(UserBase):
# id: int  # This line is redundant since the id field is already defined in the parent Players class

 
# class Config:
#    from_attributes = True


















