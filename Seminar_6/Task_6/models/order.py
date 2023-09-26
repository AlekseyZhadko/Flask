from datetime import datetime

from pydantic import BaseModel, Field


class Order(BaseModel):
    id: int
    id_user: int
    id_product: int
    date: str
    status: bool


class OrderIn(BaseModel):
    id_user: int
    id_product: int
    date: str
    status: bool
