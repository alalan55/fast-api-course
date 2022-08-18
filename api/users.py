import fastapi
# Usamos para dizer se um campo é opcional ou não
from typing import Optional, List
# Com base model nos criamos os models pra a aplicação
from pydantic import BaseModel


router = fastapi.APIRouter()


USERS = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[User])
async def get_users():
    return USERS


@router.post("/users")
async def create_users(user: User):
    USERS.append(user)
    return {"message": "Success"}


# Para passar parâmetros na rota usamos essa expressão
# @router.get("/users/{id}")
# # Pode-se usar tipagem de dados assim, além das classes, usamos o Path para dizer ao dev o que é aquele campo, além de podemos passar o menor campo para ele, que no caso aqui é 2
# async def get_user(id: int = Path(..., description="Id do usuário que será retornado", gt=2), q: str = Query(None, max_length=5)):
#     return {"user": USERS[id], "query": q}

@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": USERS[id]}
