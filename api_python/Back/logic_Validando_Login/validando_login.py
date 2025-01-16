from Back.logic_Validando_Login import BuscandoCredenciaisNoDataBase, ValidadorDeLogin

class ValidandoLogin:
    def __init__(self, usuario, senha):
        self.dados_usuario = {
            "username": str(usuario),
            "password": str(senha),
        }
        self.dados_banco = {}

    async def buscar_dados_no_bd(self):
        """
        Busca as credenciais do usuário no banco de dados.
        """
        try:
            # Fazendo a busca de dados de forma assíncrona
            instancia_bd = BuscandoCredenciaisNoDataBase(self.dados_usuario["username"])
            print(instancia_bd)
            self.dados_banco = await instancia_bd.buscar_credenciais() 
            
            if self.dados_banco != False:
                return True
            
            return False
        
        except Exception as e:
            return {"erro": f"Erro ao buscar dados no banco de dados: {e}","status":500}

    async def validar_credenciais(self):
        """
        Valida as credenciais fornecidas pelo usuário com as do banco.
        """
        try:
            lista_usuario = [self.dados_usuario["username"], self.dados_usuario["password"]]
            lista_banco = [self.dados_banco["username"], self.dados_banco["password"]]
            
            inst_validador = ValidadorDeLogin(lista_usuario, lista_banco)
            data = await inst_validador.validar_login()
            print(data)
            return data
        
        except Exception as e:
            return {"erro": f"Erro ao validar credenciais: {e}","status":500}

    async def executar(self):
        """
        Executa todo o fluxo de validação do login.
        """
        if await self.buscar_dados_no_bd() != True:  
            return {"message": "Usuário não encontrado","status":400}

        if await self.validar_credenciais() != True: 
            return {"message": "Credencial ou usuário invalído.","status":400}
        
        return [self.dados_banco["id"], self.dados_banco["credencial_JWT"]]

