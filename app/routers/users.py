from fastapi import APIRouter, Depends
from app.schemas.schema import ShowUser, User
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import user
from app.utils.oauth2 import get_current_user

router = APIRouter(
  prefix='/user',
  tags=["Users"]
)

@router.post('/', response_model=ShowUser)
def create(request: User, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return user.create(request, db)

@router.get('/{id}', response_model=ShowUser)
def show(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
  return user.show(id, db)