from typing import List

from fastapi import APIRouter

from Seminar_6.Task_6.db import database, products
from Seminar_6.Task_6.models.product import ProductIn, Product

router = APIRouter()


@router.get("/fake_products/{count}")
async def create_products(count: int):
    for i in range(count):
        query = products.insert().values(name=f'name{i}',
                                         description=f'description{i}',
                                         price=1236.123 + i, )
        await database.execute(query)
    return {'message': f'{count} fake products create'}


@router.get("/products/", response_model=List[ProductIn])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{products_id}", response_model=ProductIn)
async def read_products_id(products_id: int):
    query = products.select().where(products.c.id == products_id)
    return await database.fetch_one(query)


@router.post("/products/", response_model=Product)
async def create_products(product: ProductIn):
    query = products.insert().values(name=product.name, description=product.description, price=product.price)
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@router.put("/products/{products_id}", response_model=Product)
async def update_products(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete("/products/{products_id}")
async def delete_products(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
