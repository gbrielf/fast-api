from sqlalchemy import Column, Integer, String, Numeric, Float, Boolean, DateTime
from datetime import datetime
from core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    stock = Column(Integer, nullable=False)
    availability = Column(Boolean, default=False) # default = False: defines the field availability as True when the product was registered 
    register_data = Column(DateTime, default=datetime.utcnow) #utcnow: defines the hour when the product was registered


