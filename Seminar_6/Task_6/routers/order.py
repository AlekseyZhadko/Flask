import random
from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from Seminar_6.Task_6.db import database, products, orders, users
from Seminar_6.Task_6.models.order import OrderIn, Order
from Seminar_6.Task_6.models.product import ProductIn, Product

router = APIRouter()


@router.get("/fake_orders/{count}")
async def create_orders(count: int):
    for i in range(count):
        query = orders.insert().values(id_user=random.randint(0, 10),
                                       id_product=random.randint(0, 25),
                                       date=f'10.10.2023',
                                       status=True)
        await database.execute(query)
    return {'message': f'{count} fake orders create'}


@router.get("/orders/", response_model=List)
async def read_order():
    query = select(
        orders.c.id,
        orders.c.date,
        orders.c.status,

        # products.c.id.label('product_id'),
        # products.c.name,
        # products.c.description,
        # products.c.price

        users.c.id.lavel('user_id'),
        users.c.firstname,
        users.c.lastname
    ).join(users)
    return await database.fetch_all(query)


@router.get("/orders/{orders_id}", response_model=OrderIn)
async def read_order_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@router.post("/orders/", response_model=Order)
async def create_orders(order: OrderIn):
    query = orders.insert().values(id_user=order.id_user,
                                   id_product=order.id_product,
                                   date=order.date,
                                   status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@router.put("/orders/{orders_id}", response_model=Order)
async def update_orders(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{orders_id}")
async def delete_orders(orders_id: int):
    query = orders.delete().where(orders.c.id == orders_id)
    await database.execute(query)
    return {'message': 'Order deleted'}
