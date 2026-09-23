from sqlalchemy.future import select

from backend.database import SessionLocal
from backend.models import Customer
from backend.schemas import CustomerCreate


async def create_customer(data: CustomerCreate) -> Customer:
    async with SessionLocal() as session:
        customer = Customer(**data.model_dump())
        session.add(customer)
        await session.commit()
        await session.refresh(customer)
        return customer


async def get_customers() -> list[Customer]:
    async with SessionLocal() as session:
        result = await session.execute(select(Customer))
        return result.scalars().all()
