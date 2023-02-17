from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router= APIRouter(prefix="/users",
                    tags=["/users"],
                    responses={404: {"message":"No encontrado"}})
# Inicia el server: python - m uvicorn users:app --reload

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Juan", surname= "Crotta", url="juancruzcrotta", age= 20),
                User(id=2, name="Pedro", surname= "Alfonso", url="pedro.com",age= 33),
                User(id=3, name="Emi", surname= "Martinez", url="ema.com",age= 25)]

@router.get("/usersjson")
async def usersjson():
    return [{"name":"Juan", "surname": "Crotta", "url":"juancruzcrotta", "age": 20},
            {"name":"Pedro", "surname": "Alfonso", "url":"pedro.com","age":33},
            {"name":"Emi", "surname": "Martinez", "url":"ema.com","age":25}]
                                    
@router.get("/users/")
async def usersjson():
    return users_list

#Path
@router.get("/users/{id}")
async def user(id: int):
    users=filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

#Query
@router.get("/usersquery/")
async def user(id: int):
    return search_user(id)

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return users_list

@router.put("/user/")
async def user(user: User):

    found= False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found= True
            break  # Agrega un break para salir del ciclo si el usuario fue encontrado

    if not found:
        return {"error":404,"message":"No se ha encontrado el usuario"}
        
    return user

@router.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return users_list

#Lo anterior lo podemos meter en una funcion para no repetir
def search_user(id: int):
    users=filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


