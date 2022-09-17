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


class People(Base):
    __tablename__="people"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False, index=True)
    phone_no = Column(Integer, index=True)
    email = Column(String, nullable= False,unique=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    address = Column(String(255), unique=True, index=True)


    #soft delete
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted = Column(Boolean, default=False)


