from typing import Optional

from sqlalchemy.orm import Session

from faker import Faker

from app import crud, models

from app.schemas.product import ProductCreate


fake = Faker()


def create_random_product(db: Session) -> models.Product:
    name = fake.first_name()
    price = fake.random_int()
    product_in = ProductCreate(name=name,
                               price=price)
    return crud.product.create(db, obj_in=product_in)
