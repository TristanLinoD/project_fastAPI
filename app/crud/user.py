from fastapi import HTTPException, status
from app.schemas.schema import  User
from app.utils.hashing import Hash
from app.models import model
from sqlalchemy.orm import Session

def create(request: User, db: Session):
  hashedPassword = Hash.get_password_hash(request.password)
  new_user = model.User(name=request.name, username=request.username, password=hashedPassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def show(id:int, db: Session):
  user = db.query(model.User).filter(model.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'This user is not available {id}')
  return user