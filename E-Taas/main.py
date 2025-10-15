from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from db.database import engine, Base
from models import *
from routers import auth, users, products


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)