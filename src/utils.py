import json
import os

from src.category import Category
from src.product import Product

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

def create_objects_form_json(data):
    row_datas = []
    for row_data in data:
        products = []
        for product in row_data["products"]:
            products.append(Product(**product))
        row_data["products"] = products
        row_datas.append(Category(**row_data))
    return row_datas




if __name__ == "__main__":
    datas = read_json("../data/products.json")
    datas_product = create_objects_form_json(datas)
    print(datas_product[0].name)
    print(datas_product[0].products)