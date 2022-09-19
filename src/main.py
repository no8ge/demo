from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Optional,Union
from pprint import pprint


class Item(BaseModel):
    events: Union[Any, None] = None
    name: Union[Any, None] = None
    description: Union[Any, None] = None
    tax: Union[Any, None] = None

app = FastAPI()


@app.get("/demo/")
async def read_root():
    return {"Hello": "World"}


@app.get("/demo/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/demo/items/")
async def create_item(item: Item):
    pprint(item.dict())
    return item