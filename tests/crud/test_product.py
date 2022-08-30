from faker import Faker

from sqlalchemy.orm import Session

from app import crud
from app.schemas.product import ProductCreate, ProductUpdate

from tests import utils


fake = Faker()


def test_create_product(db: Session) -> None:
    name = fake.first_name()
    price = fake.random_int()
    product_in = ProductCreate(name=name, price=price)
    product = crud.product.create(db, obj_in=product_in)
    assert product.name == name
    assert product.price == price


def test_get_product(db: Session) -> None:
    product = utils.products.create_random_product(db)
    stored_product = crud.product.get(db, model_id=product.id)
    assert stored_product
    assert stored_product.id == product.id
    assert stored_product.price == product.price
    assert stored_product.name == product.name


def test_update_product(db: Session) -> None:
    product = utils.products.create_random_product(db)
    price2 = fake.random_int()
    product_update = ProductUpdate(id=product.id, price=price2)
    product2 = crud.product.update(db, db_obj=product, obj_in=product_update)
    assert product.id == product2.id
    assert product.name == product2.name
    assert price2 == product2.price


def test_delete_item(db: Session) -> None:
    product = utils.products.create_random_product(db)
    product2 = crud.product.remove(db, model_id=product.id)
    product3 = crud.product.get(db, model_id=product.id)
    assert product3 is None
    assert product2.id == product.id
    assert product2.name == product.name
