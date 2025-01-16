from ..logic_JWT import CriandoJWT

class RoutCriandoNovoUsuario():
    def __init__(self, username: str,password:str):
        self.nome = username
        self.senha = password
    async def startingClassValidandoFluxoCriandoUsuario(self):
        from Back.logic_Criando_Usuario import ValidandoFluxoCriandoUsuario
        instClass = ValidandoFluxoCriandoUsuario(self.nome)

        user = await instClass.executar()
        print(user)
        if (user["status"] == False): 
            return user["message"]
        instacyJWT = CriandoJWT(user["new_user"][0],user["new_user"][3],user["new_user"][1])
        return {"status": "sucess","token": instacyJWT._criando()}
       