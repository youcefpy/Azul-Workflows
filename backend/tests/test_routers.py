import pytest

from backend.config import settings
from fastapi import HTTPException, status
from backend.routers import verify_api_key
class TestRouters:
    api_key = "test-admin-api-key"
    @staticmethod
    def customer_data():
        return {
            "name": "Toto",
            "email": "toto@gmail.com",
            "phone_number": "123456789",
            "company_name": "my_company",
            "service_interest": "marketing",
            "message": "Need an agent for marketing services.",
        }
    
    async def test_api_key_valid(self,client):
         settings.ADMIN_API_KEY="admin123"
         result = await verify_api_key('admin123')
         assert result is None
    
    async def test_api_key_invalide(self,client):
        settings.ADMIN_API_KEY="admin123"
        with pytest.raises(HTTPException) as exc_info:
            await verify_api_key(x_api_key="wrong-key")
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Invalid API Key" in exc_info.value.detail 
    
    def test_create_customer(self, client):
        response = client.post("/customers", json=self.customer_data())

        assert response.status_code == status.HTTP_201_CREATED
        customer = response.json()
        assert customer["id"] > 0
        assert customer["name"] == "Toto"
        assert customer["email"] == "toto@gmail.com"
        assert customer["company_name"] == "my_company"

    def test_list_customers_requires_api_key(self, client):
        response = client.get("/customers")

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_list_customers(self, client, monkeypatch):
        monkeypatch.setattr(settings, "ADMIN_API_KEY", self.api_key)
        client.post("/customers", json=self.customer_data())

        response = client.get("/customers", headers={"X-API-Key": self.api_key})

        assert response.status_code == status.HTTP_200_OK
        customers = response.json()
        assert len(customers) == 1
        assert customers[0]["name"] == "Toto"

    def test_get_customer(self, client, monkeypatch):
        monkeypatch.setattr(settings, "ADMIN_API_KEY", self.api_key)
        created = client.post("/customers", json=self.customer_data()).json()

        response = client.get(
            f"/customer/{created['id']}",
            headers={"X-API-Key": self.api_key},
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == created["id"]
        assert response.json()["email"] == "toto@gmail.com"
