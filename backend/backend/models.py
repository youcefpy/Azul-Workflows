from sqlalchemy import Column, Integer, String
from backend.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    company_name = Column(String, nullable=True)
    service_interest = Column(String, nullable=True)
    message = Column(String, nullable=False)