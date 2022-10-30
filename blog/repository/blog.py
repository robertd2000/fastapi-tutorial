from fastapi import  status, HTTPException
from sqlalchemy.orm import Session

from blog.models import BlogModel
from blog.schemas import Blog


def get_all(db: Session):
    blogs = db.query(BlogModel).all()
    return blogs


def get_one_blog(id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found!')
    return blog


def create_blog(request: Blog, db: Session):
    new_blog = BlogModel(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blog(id: int, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found!')
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        'done': True
    }


def update_blog(id: int, request: Blog, db: Session):
    blog = db.query(BlogModel).filter(BlogModel.id == id).update(request.dict())
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found!')
    db.commit()
    return blog