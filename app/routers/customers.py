from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/customers", tags=["customers"])

def get_db():
    db = SessionLocal()
    try:   yield db
    finally: db.close()

@router.post("", status_code=status.HTTP_201_CREATED,
             response_model=schemas.CustomerOut)
def create_customer(data: schemas.CustomerCreate,
                    db: Session = Depends(get_db)):
    if db.query(models.Customer).filter_by(email=data.email).first():
        raise HTTPException(400, "Email already registered.")
    customer = models.Customer(**data.dict())
    db.add(customer); db.commit(); db.refresh(customer)
    return customer

@router.get("/{cust_id}", response_model=schemas.CustomerOut)
def get_customer(cust_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).get(cust_id)
    if not customer:
        raise HTTPException(404, "Customer not found.")
    return customer

@router.get("", response_model=list[schemas.CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@router.delete("/{cust_id}", status_code=204)
def delete_customer(cust_id: int, db: Session = Depends(get_db)):
    if db.query(models.Customer).filter_by(id=cust_id).delete() == 0:
        raise HTTPException(404, "Customer not found.")
    db.commit()
