from pydantic import BaseModel


class Product(BaseModel):
    product_category: str
    brand: str
    product_name: str
    price: str
