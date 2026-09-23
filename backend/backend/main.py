from fastapi import BackgroundTasks, Depends, FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from backend import crud, schemas
from backend.config import settings
from backend.database import SessionLocal
from backend.email import send_email_notification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

async def get_db():
    
    async with SessionLocal() as session:
        yield session


@app.post("/customers", response_model=schemas.CustomerOut)
async def create_customer(customer: schemas.CustomerCreate, background_tasks: BackgroundTasks):
    new_customer = await crud.create_customer(customer)
    background_tasks.add_task(send_email_notification, customer, True) # customer email
    background_tasks.add_task(send_email_notification, customer, False) # admin email
    print("- Background Task Queued!")
    return new_customer


async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized: Invalid API Key",
        )
    

@app.get("/customers", response_model=list[schemas.CustomerOut], dependencies=[Depends(verify_api_key)])
async def list_customers():
    return await crud.get_customers()
