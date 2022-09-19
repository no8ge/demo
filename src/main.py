from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/demo/")
async def read_root():
    return {"Hello": "World"}


@app.get("/demo/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {'skip':skip,'limit':limit}