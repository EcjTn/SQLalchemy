from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar

class UserCreate(BaseModel):
    username: str
    password: str
