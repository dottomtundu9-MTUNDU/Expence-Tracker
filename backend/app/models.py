from app.database import Base
from sqlalchemy import Column,Integer,String,Float,DateTime
from datetime import datetime

class Transaction(Base):
    __tablename__="transaction_table"
    
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    amount=Column(Float,nullable=False)
    category=Column(String,nullable=False)
    type=Column(String,nullable=False)
    date=Column(DateTime,default=datetime.now())
    