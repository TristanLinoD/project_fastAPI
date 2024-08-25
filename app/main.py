from fastapi import FastAPI
from app.routers import users, blogs, authentication
from app.models import model
from app.database import engine


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)


  





  