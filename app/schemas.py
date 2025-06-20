from pydantic import BaseModel, EmailStr, constr
from typing import List

class BranchBase(BaseModel):
    branch_code: constr(max_length=20)
    location: str

class BranchCreate(BranchBase):
    customer_id: int

class BranchOut(BranchBase):
    id: int
    class Config: orm_mode = True

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    gstin: constr(min_length=15, max_length=15)

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    branches: List[BranchOut] = []
    class Config: orm_mode = True
