from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False


items: list[Item] = []

@app.get("/")
def root():
    return {"hello": "World"}


@app.post("/items")
def create_items(item: Item) -> list[Item]:
    items.append(item)
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        return HTTPException(status_code=404, detail="Item not fount")
