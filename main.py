from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]


class Item(BaseModel):
    name: str
    price: float

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}

@app.post("/post")
def postPerson(item:Item):
    return {"Name":item.name,"Price":item.price}