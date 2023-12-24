from typing import List
from fastapi import APIRouter
from .models import New_instruments

router = APIRouter()

@router.get('/')
def router_instruments() -> List[New_instruments]:
    instruments = [
        New_instruments(id=1, name='piano', price=500, discounts=15),
        New_instruments(id=1, name='guitar', price=350, discounts=10)
    ]
    return instruments
