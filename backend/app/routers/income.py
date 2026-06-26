from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

router=APIRouter(prefix="/income",tags=["income Transaction"])

@router.post("")
def add_income(title:str,amount:float,type:str,category:str,db:Session=Depends(get_db)):
    income=models.Transaction(title=title,amount=amount,type="income",category=category)
    db.add(income)
    db.commit()
    db.refresh(income)
    return{
        "income":income,
        "message":"the income is successfull added✅"
    }
    
@router.get("")
def show_all_income(db:Session=Depends(get_db)):
    income=db.query(models.Transaction).all()
    return income

    
@router.get("/{id}")
def show_income(id:int,db:Session=Depends(get_db)):
    income=db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    return income


@router.put("/{id}")
def modify_income(id:int,title:str,amount:float,type:str,category:str,db:Session=Depends(get_db)):
    income=db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    income.title=title
    income.amount=amount
    income.type="income"
    income.category=category
        
    db.commit()
    db.refresh(income)
    return{
        "message":"the income is ssuccesfull updated✅"
    }    

@router.delete("/{id}")
def delete_income(id:int,db:Session=Depends(get_db)):
    income=db.query(models.Transaction).filter(models.Transaction.id==id).delete(synchronize_session=True)
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    return {
        "message":"the income is ssuccesfull updated✅"
    }
    