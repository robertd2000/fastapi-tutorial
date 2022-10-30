from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from blog.database import Base


class BlogModel(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("UserModel", back_populates="blogs")
    

class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("BlogModel", back_populates="author")
