from backend.crud import create_customer, get_customer, get_customers

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

