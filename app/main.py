from typing import Union

from fastapi import FastAPI

from app.api.api_v1.api import router as api_router


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(api_router, prefix="/api/v1")

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}