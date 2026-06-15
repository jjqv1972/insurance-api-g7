from sqlalchemy import Column, Integer, Float
from database import Base

class Insurance(Base):
    __tablename__ = "insurance"
    
    id = Column(Integer, primary_key=True, index=True)
    smoker = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    bmi = Column(Float, nullable=False)
    charges = Column(Float, nullable=True)