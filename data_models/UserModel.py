from uuid import UUID

from pydantic import BaseModel


class UserModel(BaseModel):
    age: int
    address: str

class UserCreate(UserModel):
    pass

class UserGet(UserModel):
    id: UUID