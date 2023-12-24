from pydantic import BaseModel
from typing import Optional


class Basemodel_instruments(BaseModel):
    id: int
    name: str
    condition: str
    price: int
    discounts: int

class New_instruments(BaseModel):
    name: str
    condition: str
    price: int
    discounts: int