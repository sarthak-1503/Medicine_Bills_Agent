from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class MedicineBill(BaseModel):
    bill_number: Optional[str] = Field(..., description="Unique identifier for the bill")
    bill_date: Optional[str] = Field(..., description="Date when the bill was generated")
    chemist_name: Optional[str] = Field(..., description="Name of the chemist issuing the bill")
    amount: Optional[float] = Field(..., description="Total amount of the bill")
    gst: Optional[float] = Field(..., description="Goods and Services Tax applied to the bill")
    prescribed_on: Optional[str] = Field(..., description="Date when the medicine was prescribed")
    prescribed_by: Optional[str] = Field(..., description="Name of the doctor who prescribed the medicine")


