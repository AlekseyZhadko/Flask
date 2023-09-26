from typing import List

from fastapi import APIRouter

from Seminar_6.Task_6.db import database, users
from Seminar_6.Task_6.models.user import User, UserIn, UserOut

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(firstname=f'firstname{i}',
                                      lastname=f'lastname{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f"123456{i}", )
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.get("/users/", response_model=List[UserOut])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
