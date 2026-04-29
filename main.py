from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # הוספנו כדי להציג את האתר
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- דף הבית של האתר ---
@app.get("/")
async def read_root():
    # השורה הזו שולחת את הקובץ index.html כשנכנסים לכתובת האתר
    return FileResponse('index.html')
@app.get("/admin")
async def read_admin():
    return FileResponse('admin.html')

# --- המודלים והלוגיקה שלך (לא נגענו) ---
class Booking(BaseModel):
    id: Optional[int] = None
    customer_name: str
    customer_phone: str
    check_in: str
    check_out: str
    notes: Optional[str] = ""
    status: Optional[str] = "חדש"

bookings_db = []
id_counter = 1

@app.get("/bookings/", response_model=List[Booking])
async def get_bookings():
    return bookings_db

@app.post("/bookings/")
async def create_booking(booking: Booking):
    global id_counter
    new_booking = booking.dict()
    new_booking["id"] = id_counter
    id_counter += 1
    bookings_db.append(new_booking)
    return new_booking

@app.patch("/bookings/{booking_id}")
async def update_status(booking_id: int, status: str):
    for b in bookings_db:
        if b["id"] == booking_id:
            b["status"] = status
            return b
    return {"error": "לא נמצא"}

@app.delete("/bookings/{booking_id}")
async def delete_booking(booking_id: int):
    global bookings_db
    bookings_db = [b for b in bookings_db if b["id"] != booking_id]
    return {"message": "נמחק בהצלחה"}