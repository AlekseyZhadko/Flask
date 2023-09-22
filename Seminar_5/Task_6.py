from http.client import HTTPException

import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app_api = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

users = []


class User_out(BaseModel):
    id: int
    name: str
    email: str


class User_in(BaseModel):
    name: str
    email: str
    password: str


class User(User_in):
    id: int


for i in range(10):
    users.append(User(
        id=i + 1,
        name=f'name{i + 1}',
        email=f'email{i + 1}@mail.ru',
        password='123'
    ))


@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post("/", response_class=HTMLResponse)
async def user(request: Request, add_name=Form(), add_email=Form(), add_password=Form()):
    print(type(add_name))
    print(type(add_email))
    print(type(add_password))
    users.append(
        User(id=len(users) + 1, name=add_name, email=add_email, password=add_password))
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put("/user/", response_model=list[User])
async def update_user(user_id: int, new_user: User_in):
    for i in range(0, len(users)):
        if users[i].id == user_id:
            current_user = users[user_id - 1]
            current_user.name = new_user.name
            current_user.email = new_user.email
            current_user.password = new_user.password
            return current_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/", response_model=dict)
async def remove_user(user_id: int):
    for i in range(0, len(users)):
        if users[i].id == user_id:
            users.remove(users[i])
            return {"message": "User was deleted"}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == '__main__':
    uvicorn.run(
        "Task_6:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
