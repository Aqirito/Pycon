# -- coding: utf-8 --

from datetime import date, datetime
from sqlalchemy import (
    String,
    Integer,
    Column,
    DateTime,
    Boolean, 
    ForeignKey,      
)
from src.models.db.base_class import Base


class Companies(Base):
    __tablename__="companies"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    company_phone_no = Column(Integer, nullable=False, index=True)
    address = Column(String(255), nullable=False, unique=True, index=True)

    #soft delete
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted = Column(Boolean, default=False)


