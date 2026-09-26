from fastapi import APIRouter, BackgroundTasks, Depends, Header, HTTPException, status

from backend import crud, schemas
from backend.config import settings
from backend.email import send_email_notification

router = APIRouter()

@router.post("/customers", response_model=schemas.CustomerOut, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: schemas.CustomerCreate, background_tasks: BackgroundTasks):
    new_customer = await crud.create_customer(customer)
    background_tasks.add_task(send_email_notification, new_customer, True)  # customer email
    background_tasks.add_task(send_email_notification, new_customer, False)  # admin email
    print("- Background Task Queued!")
    return new_customer


async def verify_api_key(x_api_key: str = Header(...))->None:
    if x_api_key != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid API Key",
        )
    

@router.get("/customers", response_model=list[schemas.CustomerOut], dependencies=[Depends(verify_api_key)])
async def list_customers():
    return await crud.get_customers()

@router.get('/customer/{id}', response_model=schemas.CustomerOut, dependencies=[Depends(verify_api_key)])
async def get_customer(id: int):
    return await crud.get_customer(id)
