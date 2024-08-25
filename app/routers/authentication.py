from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models import model
from sqlalchemy.orm import Session
from app.utils.hashing import Hash
from app.utils import token
from app.schemas.schema import Token


router = APIRouter(
  prefix='/login',
  tags=['Authentication']
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Token:
  user = db.query(model.User).filter(model.User.username == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid User')
  if not Hash.verify_password(request.password, user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect Password')
  
  access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = token.create_access_token(
      data={"sub": user.username}, expires_delta=access_token_expires
  )
  return Token(access_token=access_token, token_type="bearer")