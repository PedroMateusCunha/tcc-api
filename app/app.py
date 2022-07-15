from collections import UserString
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def root():
    return {"message": "Hello World"}

# Criar Model
class User(BaseModel):
    id: int
    email: str
    password: str

# Criar Base de Dados
database = [
    User(id=1, email="teste1@teste.com", password="teste1@123"),
    User(id=2, email="teste2@teste.com", password="teste2@123"),
    User(id=3, email="teste3@teste.com", password="teste3@123"),
    User(id=4, email="teste4@teste.com", password="teste4@123"),
    User(id=5, email="teste5@teste.com", password="teste5@123"),
    User(id=6, email="teste6@teste.com", password="teste6@123")
]

# Rota Get All User
@app.get("/users")
def get_all_users():
    return database

# Rota Get User por ID
@app.get("/user/{id_user}")
def get_user_id(id_user: int):
    for user in database:
        if (user == id_user):
            return user
    return {"Status": 404, "Message":"User not found"}

# Rota de Inserir Usuário
@app.post("/user")
def add_user(user: User):
    database.append(user)
    return user