from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    gstin = Column(String(15),  unique=True, nullable=False)

    branches = relationship("Branch", back_populates="customer",
                            cascade="all, delete")

class Branch(Base):
    __tablename__ = "branches"

    id          = Column(Integer, primary_key=True, index=True)
    branch_code = Column(String(20), nullable=False)
    location    = Column(String(120), nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id",
                                             ondelete="CASCADE"))
    customer    = relationship("Customer", back_populates="branches")
