import json
import uuid
from typing import Union
from fastapi import FastAPI, Request, HTTPException
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


@app.put("/LabelingEmotionsDatabase/{item_id}", response_model=str, status_code=201)
async def update_item(item_id: str, item: Request):
    labels = await item.json()
    try:
        json_object = json.loads(labels)
    except (ValueError, TypeError):
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON payload format"
        )

    with open(f"{uuid.uuid4()}.json", "w") as file_write:
        json.dump(json_object, file_write)
    return item_id
