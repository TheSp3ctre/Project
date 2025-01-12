from Back.logic_Validando_Login import ValidandoLogin
from Back.logic_JWT import CriandoJWT

class RoutValidandoLogin():
    def __init__(self, nome_do_usuario: str, senha_do_usuario: str):
        self.nome_do_usuario = nome_do_usuario
        self.senha_do_usuario = senha_do_usuario
    
    async def _startingClassValidandoLogin(self):

        instClass = ValidandoLogin(self.nome_do_usuario, self.senha_do_usuario)
        val = await instClass.executar()

        if val != False:
            return await self._startingClassCriandoJWT(val[0], val[1])
        
        return {"status": "error", "message": "Usuário ou senha inválidos"}
    
    async def _startingClassCriandoJWT(self, id, credencial_JWT):
        instClass = CriandoJWT(id, credencial_JWT)
        return await instClass._criando()


    
    