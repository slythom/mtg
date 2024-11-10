# activate venv
from scryfall import *
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    result = 'Successfully connected to the API'
    return result

@app.get("/sets")
def read_sets():
    result = set_list()
    return result

@app.get("/set_cards")
def read_set_cards():
    result = set_card_list()
    return result

#FastAPI example:
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}