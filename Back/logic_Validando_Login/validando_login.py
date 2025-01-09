from Back.logic_Validando_Login import BuscandoCredenciaisNoDataBase, ValidadorDeLogin

class ValidandoLogin:
    def __init__(self, usuario, senha):
        self.dados_usuario = {
            "nome": str(usuario),
            "senha": str(senha),
        }
        self.dados_banco = {}

    async def buscar_dados_no_bd(self):
        """
        Busca as credenciais do usuário no banco de dados.
        """
        try:
            # Fazendo a busca de dados de forma assíncrona
            instancia_bd = BuscandoCredenciaisNoDataBase(self.dados_usuario["nome"])

            self.dados_banco = await instancia_bd.buscar_credenciais() 
            
            if self.dados_banco != False:
                return True
            
            return False
        
        except Exception as e:
            return {"erro": f"Erro ao buscar dados no banco de dados: {e}"}

    async def validar_credenciais(self):
        """
        Valida as credenciais fornecidas pelo usuário com as do banco.
        """
        try:
            lista_usuario = [self.dados_usuario["nome"], self.dados_usuario["senha"]]
            lista_banco = [self.dados_banco["nome"], self.dados_banco["senha"]]
            
            inst_validador = ValidadorDeLogin(lista_usuario, lista_banco)
            return await inst_validador.validar_login() 
        
        except Exception as e:
            return {"erro": f"Erro ao validar credenciais: {e}"}

    async def executar(self):
        """
        Executa todo o fluxo de validação do login.
        """
        print("1")
        if await self.buscar_dados_no_bd() != True:  
            return False
        print("2")
        if await self.validar_credenciais() != True:  
            return False
        print("3")
        return [self.dados_banco["id"], self.dados_banco["credencial_JWT"]]

