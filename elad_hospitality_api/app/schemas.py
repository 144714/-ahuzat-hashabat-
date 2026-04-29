from pydantic import BaseModel
from datetime import date
from typing import Optional

class BookingBase(BaseModel):
    customer_name: str
    customer_phone: str
    check_in: date
    check_out: date
    notes: Optional[str] = None

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int
    total_price: float
    is_confirmed: bool

    class Config:
        from_attributes = True