"""
AccountFactory class using FactoryBoy

Documentation on Faker Providers:
    https://faker.readthedocs.io/en/master/providers/baseprovider.html

Documentation on Fuzzy Attributes:
    https://factoryboy.readthedocs.io/en/stable/fuzzy.html

"""
import factory
from datetime import date
from factory.fuzzy import FuzzyChoice, FuzzyDate
from backend.models import Customer


class CustomerFactory(factory.Factory):
    """ Creates fake Accounts """

    class Meta:
        model = Customer

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("name")
    email = factory.Faker("email")
    phone_number = factory.Faker("phone_number")
    company_name = factory.Faker('company')
    service_interest = FuzzyChoice(choices=[
        "lead_lifecycle_management",
        "content_operations_scale",
        "document_intelligence",
        "customer_support_knowledge",
        "data_hygiene_reporting",
        "custom_agentic_workflows"
    ])
    message = factory.Faker("text")