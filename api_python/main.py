import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()


# Modelo de requisição para criação de usuário
class UserCreationRequest(BaseModel):
    username: str
    password: str
# Endpoint de criação de usuário
@app.post("/auth/register/user")
async def creation(creation_request: UserCreationRequest):
    from Back.routes import RoutCriandoNovoUsuario
    
    instClass = RoutCriandoNovoUsuario(creation_request.username)

    return await instClass.startingClassValidandoFluxoCriandoUsuario()


# Modelo de requisição para login
class LoginAuthenticactionRequest(BaseModel):
    username: str = Field(alias="nome")
    password: str  = Field(alias='senha')
# Endpoint de autenticação
@app.post("/auth/login")
async def login(auth_request: LoginAuthenticactionRequest):  
    from Back.routes.Rota_ValidandoLogin import RoutValidandoLogin
    instClass = RoutValidandoLogin(auth_request.username, auth_request.password)

    return await instClass._startingClassValidandoLogin()

if __name__ == "__main__":
    uvicorn.run(app, port=8000,reload=False)
