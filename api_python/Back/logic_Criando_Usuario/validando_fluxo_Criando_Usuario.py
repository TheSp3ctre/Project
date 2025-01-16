class ValidandoFluxoCriandoUsuario():
    def __init__(self, nome_do_usuario: str):
        """Listas para armazenar os dados processados"""
        self.nome_do_usuario = nome_do_usuario
        self.senha_e_credencial_geradas = []  # Armazena senha e credencial geradas
        self.senha_e_credencial_encriptadas = []  # Armazena senha e credencial encriptadas
        self.senha_original = None  # Armazena a senha original

    async def gerar_senha_e_credencial(self):
        """Gera senha e credencial usando a classe CriandoSenhaeCredencial."""
        try:
            from Back.logic_Criando_Usuario import CriandoSenhaeCredencial

            inst = CriandoSenhaeCredencial()
            await inst._criandoSenhaeCredencial()
            self.senha_e_credencial_geradas = inst._armazenandoSenhaeCredencialParaUso()

            if self.senha_e_credencial_geradas == []:  # Caso retorne vazia
                return False
            
            # Armazena a senha original
            self.senha_original = self.senha_e_credencial_geradas[0]
            return True
        
        except ValueError as e:
            return False

    async def encriptar_senha_e_credencial(self):
        """Encripta a senha e a credencial geradas."""
        try:
            from Back.logic_Criando_Usuario import EncriptandoSenhaeCredencial

            # Acessando e inserindo os dados da lista nas variáveis
            senha = str(self.senha_e_credencial_geradas[0])
            credencial = str(self.senha_e_credencial_geradas[1])

            inst = EncriptandoSenhaeCredencial(senha, credencial)
            await inst._criandoHashsenhaEcredencial()
            self.senha_e_credencial_encriptadas = inst._armazenandoSenhaEcredencialhashsParaUso()

            if self.senha_e_credencial_encriptadas == []:  # Caso retorne vazia
                return False

            return True
        
        except ValueError as e:
            return False

    async def criando_novo_usuario(self):
        """Cria um novo usuário e insere no banco de dados."""
        try:
            from Back.logic_Criando_Usuario import CreateNovoUsuario

            senha = str(self.senha_e_credencial_encriptadas[0])
            credencial = str(self.senha_e_credencial_encriptadas[1])

            inst = CreateNovoUsuario(self.nome_do_usuario, senha, credencial)
            result = await inst._inserindoDadosnoBD()
            
            self.result = result 
            return True
        
        except ValueError as e:
            return False

    async def executar(self):

        if await self.gerar_senha_e_credencial() != True:
            return False

        if await self.encriptar_senha_e_credencial() != True:
            return False

        if await self.criando_novo_usuario() != True:
            return False

        return self.result