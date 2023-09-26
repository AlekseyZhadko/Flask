from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    username: str
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)


class UserIn(BaseModel):
    username: str
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)
