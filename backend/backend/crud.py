from collections.abc import Sequence

from fastapi import HTTPException, status
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


async def get_customers() -> Sequence[Customer]:
    async with SessionLocal() as session:
        result = await session.execute(select(Customer))
        return result.scalars().all()

async def get_customer(id: int) -> Customer | None:
    async with SessionLocal() as session:
        result = await session.execute(
            select(Customer).where(Customer.id==id)
            )
        customer = result.scalar_one_or_none()
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer Not found",
            )
        return customer

async def delete_customer(id:int) -> None:
    async with SessionLocal() as session:
        query = await session.execute(
        select(Customer).where(Customer.id==id)
        )
        customer = query.scalar_one_or_none()

        if customer is None : 
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Customer Not found"
            )
        await session.delete(customer)
        await session.commit()

        
