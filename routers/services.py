from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional,Annotated
from sqlalchemy.orm import Session
from databases import SessionLocal
from models import Services

app = FastAPI()

router = APIRouter(
    prefix="/servises",
    tags=["services"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ServiceRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed by user", default=None)
    name: str = Field(min_length=3)
    phone_number: str = Field(min_length=10)
    address: str = Field(min_length=3, max_length=60)
    product: str =Field(min_length=2, max_length=50)

    # this for:-- Data Documentation and User Experience.
    class Config():
        json_schema_extra = {
            "example": {
                "name": "Ashraf",
                "phone_number": "0123456789",
                "address": " 58, Pratap Nagar, Delhi, Pincode: 110091",
                "product": "air conditioner",
                "isPaid": "True/False (Optional)"
            }
        }
        

@router.get("/")
async def see_all_service(db: db_dependency):
    all_service = db.query(Services).all()
    return all_service
    raise HTTPException(status_code=404, detail="Not found")

@router.post("/request_services")
async def request_service(db: db_dependency, req_service: ServiceRequest):
    new_service = Services(**req_service.model_dump())

    db.add(new_service)
    db.commit()
