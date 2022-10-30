from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from blog.models import UserModel
from blog.schemas import User
from ..hashing import Hash


def get_one_user(id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found!')
    return user

def create_new_user(request: User, db: Session):
    new_user = UserModel(name=request.email, email=request.email, password=Hash.bcrypt(password=request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user