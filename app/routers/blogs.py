from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.schema import ShowBlog, Blog, User
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.oauth2 import get_current_user
from app.crud import blog

router = APIRouter(
  prefix="/blog",
  tags=["Blogs"]
)

@router.get('/', response_model=List[ShowBlog])  
def all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  print(current_user)
  return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  print(current_user)
  return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=ShowBlog)  
def show(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return blog.get_blog(id, db)
  