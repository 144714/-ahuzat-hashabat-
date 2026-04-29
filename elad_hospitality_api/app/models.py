from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from .database import Base

class HospitalitySettings(Base):
    __tablename__ = "settings"
    
    id = Column(Integer, primary_key=True, index=True)
    property_name = Column(String, default="מתחם אירוח אלעד")
    base_price_weekday = Column(Float)  # מחיר ללילה באמצע שבוע
    base_price_shabbat = Column(Float)  # מחיר גלובלי לשבת

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_phone = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    total_price = Column(Float)
    notes = Column(String, nullable=True) # בקשות מיוחדות (פלטות, מיחם וכו')
    is_confirmed = Column(Boolean, default=False)