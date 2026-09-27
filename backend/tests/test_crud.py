import pytest
from backend.crud import create_customer, delete_customer, get_customer, get_customers
from fastapi import HTTPException, status

from .factories import CustomerFactory


class TestCrudCustomer:

    async def test_create_customer(self,client, db):
        data = CustomerFactory()

        # create create_customer
        customer = await create_customer(data)

        assert customer.id == data.id
        assert customer.name == data.name
        assert customer.email == data.email
        assert customer.phone_number == data.phone_number
        assert customer.company_name == data.company_name
        assert customer.service_interest == data.service_interest
        assert customer.message == data.message

    async def test_get_customers(self,db):
        list_customers = [await create_customer(CustomerFactory()) for _ in range(10)]
        assert list_customers is not None
        customers = await get_customers()
        assert len(customers) == 10

    async def test_get_customer(self,db):
        data = CustomerFactory()
        customer_create = await create_customer(data)
        id = customer_create.id
        customer = await get_customer(id)
        assert customer.id is not None
        assert customer.id == data.id
        assert customer.name == data.name
        assert customer.email == data.email
        assert customer.phone_number == data.phone_number

    async def test_customer_not_found(self,db):
        id = 2144142214
        with pytest.raises(HTTPException) as exec_info:
            await get_customer(id=id)
        assert exec_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert "Customer Not found" in exec_info.value.detail


    async def test_delete_customer(self,db):
        data = CustomerFactory()
        
        customer = await create_customer(data)
        
        customers = await get_customers()
        
        assert len(customers) == 1
        c = await get_customer(customer.id)
        assert c is not None
        assert c.name == customer.name
        assert c.id == customer.id
        assert c.email == customer.email
        await delete_customer(customer.id)
        custo = await get_customers()
        assert len(custo) == 0


        
