from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Union


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.get("/demo/")
async def read_root():
    return {"Hello": "World"}


@app.get("/demo/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/demo/items/")
async def create_item(item: Item):
    return item