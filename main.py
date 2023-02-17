from fastapi import FastAPI
from routers import products,users,basic_auth_users,jwt_auth_users,users_db
from fastapi.staticfiles import StaticFiles

app= FastAPI()

#Routers para agregar el resto de app a esta
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

#Para agregar una imagen
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return { "url_curso":"www.google.com"}


#Inicias el servidor con: python -m uvicorn main:app --reload
#La documentacion la podes ver en: http://127.0.0.1:8000/docs http://127.0.0.1:8000/redoc