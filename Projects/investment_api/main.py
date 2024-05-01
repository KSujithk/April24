from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    category: str
    description: str


@app.get("/")
def read_home():
    """This method reprsents call to the home"""
    return {"Hello World": "Fast API"}


# @app.post("/Products")
# def create_product(id:int, name:str, category: str, description: str):
#     """This method creates product
#     """
#     print(id,name, category,description)
#     # save this to database
#     return {"Message", "Created"}

@app.post("/Product")
def create_product(product:Product):
    print(product.id, product.name,product.category,product.description)
    return { "Message", "Created"}


def create_dummy_product(id:int, text:str):
    product = Product(id=id,name=text,category=text,description=text)
    return product

@app.get("/Product")
async def get_all_products() -> list[Product]:
    products = []
    for index in range(1,11):
        products.append(create_dummy_product(index, "test"))
    return products




