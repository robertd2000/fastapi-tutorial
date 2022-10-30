from datetime import datetime

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BlogModel(BaseModel):
    title: str
    author: str
    date: datetime | None = None


@app.get('/blog')
async def index(q: str | None = None, limit: int = 100, ):
    if q:
        return {
            'data': q
        }
    return {
        'data': 'list',
        "limit": limit,
    }


@app.get('/blog/{blog_id}')
async def about(blog_id: int):
    return {
        'data': blog_id
    }


@app.post('/post')
async def create_blog(body: BlogModel):
    return {
        'post': body
    }


