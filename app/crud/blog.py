from app.models import model
from sqlalchemy.orm import Session
from app.schemas.schema import Blog
from fastapi import HTTPException, status

def get_all(db: Session):
  blogs = db.query(model.Blog).all()
  return blogs

def create(request: Blog, db: Session):
  new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def delete(id:int, db: Session):
  blog = db.query(model.Blog).filter(model.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
  blog.delete(synchronize_session=False)
  db.commit()
  return {f'Blog deleted'}

def update(id, request:Blog, db: Session):
  blog = db.query(model.Blog).filter(model.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
  blog.update({'title':request.title, 'body':request.title, 'published':request.published})
  db.commit()
  return {'Blog updated'}

def get_blog(id:int, db: Session):
  blog = db.query(model.Blog).filter(model.Blog.id == id).first()
  if not blog:
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'detail': f'Blog with the id {id} is not available'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
  return blog