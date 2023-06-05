import json
import uuid
from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    content: Union[str, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/LabelingEmotionsDatabase/{item_id}", response_model=str, status_code=201)
async def update_item(item_id: str, item: Request):
    labels = await item.json()
    with open(f"{uuid.uuid4()}.json", "w") as file_write:
        json.dump(labels, file_write)
    return item_id
