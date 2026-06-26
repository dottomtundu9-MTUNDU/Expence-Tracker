from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import models
from app.database import get_db

router=APIRouter(prefix="/Expence",tags=["Expence Transaction"])

@router.post("")
def add_expence(title:str,amount:float,type:str,category:str,db:Session=Depends(get_db)):
    expence=models.Transaction(title=title,amount=amount,type="expence",category=category)
    db.add(expence)
    db.commit()
    db.refresh(expence)
    return{
        "income":expence,
        "message":"the expence is ssuccesfull added✅"
    }
    
@router.get("")
def show_all_expence(db:Session=Depends(get_db)):
    expence=db.query(models.Transaction).all()
    return expence

    
@router.get("/{id}")
def show_expence(id:int,db:Session=Depends(get_db)):
    expence=db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not expence:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    return expence


@router.put("/{id}")
def modify_expence(id:int,title:str,amount:float,type:str,category:str,db:Session=Depends(get_db)):
    expence=db.query(models.Transaction).filter(models.Transaction.id==id).first()
    if not expence:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    expence.title=title
    expence.amount=amount
    expence.type="expence"
    expence.category=category
        
    db.commit()
    db.refresh(expence)
    return{
        "message":"the expence is ssuccesfull updated✅"
    }    

@router.delete("/{id}")
def delete_expence(id:int,db:Session=Depends(get_db)):
    expence=db.query(models.Transaction).filter(models.Transaction.id==id).delete(synchronize_session=True)
    if not expence:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the requested income with id {id} not found")
    return {
        "message":"the expence is ssuccesfull updated✅"
    }
    