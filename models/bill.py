from pydantic import BaseModel, Field
from datetime import date

class MedicineBill :
    bill_number: str = Field(..., description="Unique identifier for the bill")
    bill_date: date = Field(..., description="Date when the bill was generated")
    chemist_name: str = Field(..., description="Name of the chemist issuing the bill")
    amount: float = Field(..., description="Total amount of the bill")
    gst: float = Field(..., description="Goods and Services Tax applied to the bill")
    prescribed_on: date = Field(..., description="Date when the medicine was prescribed")
    prescribed_by: str = Field(..., description="Name of the doctor who prescribed the medicine")


