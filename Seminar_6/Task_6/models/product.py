import datetime

from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str = Field(max_length=32)
    description: str = Field(max_length=250)
    price: float


class ProductIn(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=250)
    price: float
