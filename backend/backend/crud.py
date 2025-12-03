from sqlalchemy.future import select
from backend.models import Customer
from backend.database import SessionLocal
from backend.schemas import CustomerCreate
from typing import List


async def create_customer(data: CustomerCreate) -> Customer:
    async with SessionLocal() as session:
        customer = Customer(**data.dict())
        session.add(customer)
        await session.commit()
        await session.refresh(customer)
        return customer


async def get_customers() -> List[Customer]:
    async with SessionLocal() as session:
        result = await session.execute(select(Customer))
        return result.scalars().all()
