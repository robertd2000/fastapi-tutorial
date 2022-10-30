from fastapi import APIRouter

from fastapi import  Depends, status
from sqlalchemy.orm import Session
from blog.oauth2 import get_current_user

from blog.repository.blog import create_blog, delete_blog, get_all, get_one_blog, update_blog

from ..database import get_db
from ..schemas import Blog, ShowBlog, User

router = APIRouter(prefix='/blog', tags=['blogs'])


@router.get('/', response_model=list[ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    return get_all(db=db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_blog(id, db: Session = Depends(get_db)):
    return get_one_blog(id, db=db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_blog(request=request, db=db)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return delete_blog(id, db=db)
    

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_blog(id, request=request, db=db)

    