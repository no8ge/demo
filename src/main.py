from pprint import pprint
from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/demo/")
async def read_root():
    return {"Hello": "World"}


@app.get("/demo/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/demo/items")
async def anythings(item: dict):
    pprint(item)
    return item
