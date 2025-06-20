from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/branches", tags=["branches"])

def get_db():
    db = SessionLocal()
    try:   yield db
    finally: db.close()

@router.post("", status_code=status.HTTP_201_CREATED,
             response_model=schemas.BranchOut)
def create_branch(data: schemas.BranchCreate, db: Session = Depends(get_db)):
    if not db.query(models.Customer).get(data.customer_id):
        raise HTTPException(404, "Customer not found.")
    branch = models.Branch(**data.dict())
    db.add(branch); db.commit(); db.refresh(branch)
    return branch

@router.get("/{branch_id}", response_model=schemas.BranchOut)
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = db.query(models.Branch).get(branch_id)
    if not branch:
        raise HTTPException(404, "Branch not found.")
    return branch

@router.get("", response_model=list[schemas.BranchOut])
def list_branches(customer_id: int | None = Query(None),
                  db: Session = Depends(get_db)):
    q = db.query(models.Branch)
    if customer_id:
        q = q.filter(models.Branch.customer_id == customer_id)
    return q.all()
