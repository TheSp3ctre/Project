class RoutCriandoNovoUsuario():
    def __init__(self, nome: str):
        self.nome = nome
    
    async def startingClassValidandoFluxoCriandoUsuario(self):
        from Back.logic_Criando_Usuario import ValidandoFluxoCriandoUsuario
        instClass = ValidandoFluxoCriandoUsuario(self.nome)


        val = await instClass.executar()  

        print(val)
        if not val:
            return {"status": "False", "nome_do_usuario": self.nome, "senha": val}

        return {"status": "True", "nome_do_usuario": self.nome, "senha": val}
