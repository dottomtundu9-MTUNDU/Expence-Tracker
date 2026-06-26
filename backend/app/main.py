from fastapi import FastAPI
from app.routers import expence,dashbord,income
from app.database import engine,Base


Base.metadata.create_all(engine)

app =FastAPI(title="EXPENCE TRACKER",description="access your bussness smoothly")

app.include_router(income.router)
app.include_router(expence.router)
app.include_router(dashbord.router)