from backend.email import admin_email, customer_email, send_email_notification

from .factories import CustomerFactory


class TestEmailCustomer:
    """Test email customer"""


    def test_customer_email(self):
        """An email is send to admin that telling him the name of the customer"""
        customer = CustomerFactory()

        body_email = customer_email(customer)

        assert body_email is not None 
        assert customer.name in body_email 
        assert customer.email in body_email
        assert customer.phone_number in body_email
        assert customer.company_name in body_email
        assert customer.service_interest in body_email
        assert customer.message in body_email

    def test_admin_email(self):
        customer = CustomerFactory()

        body_email = admin_email(customer)
        
        assert body_email is not None 
        assert customer.name in body_email 
        assert customer.email in body_email
        assert customer.phone_number in body_email
        assert customer.company_name in body_email
        assert customer.service_interest in body_email
        assert customer.message in body_email

    
    # def test_send_email_notification_is_customer(self):
    #     """
    #     Test send email to a customer from admin
    #     """
    #     customer = CustomerFactory()
    #     send_email_notification(customer=customer,is_customer=True)

    
    # def test_send_email_notification_is_admin(self):
    #     """
    #     Test test email to admin to telling him that a new customer 
    #     """

    
    # def test_error_send_email(self):
    #     ...