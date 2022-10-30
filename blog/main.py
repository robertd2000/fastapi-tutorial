from fastapi import FastAPI


from .database import Base, engine
from .routers import blog, user, auth

app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

