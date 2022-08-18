# Usamos para dizer se um campo é opcional ou não
from typing import Optional, List
from fastapi import FastAPI, Path, Query

# Com base model nos criamos os models pra a aplicação
from pydantic import BaseModel

app = FastAPI()


USERS = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return USERS


@app.post("/users")
async def create_users(user: User):
    USERS.append(user)
    return {"message": "Success"}


@app.get("/users/{id}")  # Para passar parâmetros na rota usamos essa expressão
# Pode-se usar tipagem de dados assim, além das classes, usamos o Path para dizer ao dev o que é aquele campo, além de podemos passar o menor campo para ele, que no caso aqui é 2
async def get_user(id: int = Path(..., description="Id do usuário que será retornado", gt=2), q: str = Query(None, max_length=5)):
    return {"user": USERS[id], "query": q}
