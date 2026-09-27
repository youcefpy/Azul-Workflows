from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str | None = None
    company_name: str | None = None
    service_interest: str
    message: str


class CustomerOut(CustomerCreate):
    id: int

    class Config:
        orm_mode = True
