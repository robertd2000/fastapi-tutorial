from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog.repository.user import create_new_user, get_one_user
from ..schemas import ShowUser, User
from ..database import get_db


router = APIRouter(prefix='/user', tags=['users'])


@router.post('/', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    return create_new_user(request=request, db=db)


@router.get('/{id}', response_model=ShowUser, status_code=status.HTTP_200_OK)
def get_user(id, db: Session = Depends(get_db)):
    return get_one_user(id, db=db)