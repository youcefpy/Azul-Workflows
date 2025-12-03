from pydantic import BaseModel, EmailStr
from typing import Optional


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None
    company_name: Optional[str] = None
    service_interest: str
    message: str


class CustomerOut(CustomerCreate):
    id: int

    class Config:
        orm_mode = True
