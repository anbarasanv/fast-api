from .schema import Product
from fastapi import APIRouter

router = APIRouter(
    prefix="/product",
    tags=['Produc']
)


@router.get("/")
def home_page():
    return {"greet": "Welcom"}


@router.post("/")
def create_product(product: Product):
    return product
