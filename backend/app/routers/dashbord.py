from fastapi import APIRouter,Depends
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models

router=APIRouter(prefix="/Dashbord",tags=["Dashbord"])
    
@router.get("/")
def get_dashbord_summary(db:Session=Depends(get_db)):
    total_income=db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type=="income").scalar()or 0.0
    total_expence=db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type=="expence").scalar()or 0.0
    current_balance=total_income-total_expence
    transaction_summary=db.query(models.Transaction).order_by(models.Transaction.date.asc()).all()
    return{
        "total_income":total_income,
        "total_expence":total_expence,
        "current_balance":current_balance,
        "transaction_summary":transaction_summary
    }