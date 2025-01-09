import asyncio
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class ValidadorDeLogin:
    def __init__(self, dados_usuario=None, dados_registrados=None):
        self.dados_usuario = dados_usuario or []
        self.dados_registrados = dados_registrados or []

    async def separar_dados(self):
        
        usuario_nome, usuario_senha = self.dados_usuario
        registrado_nome, registrado_senha = self.dados_registrados

        return await self.comparar_dados(usuario_nome, usuario_senha, registrado_nome, registrado_senha)

    async def comparar_dados(self, usuario_nome, usuario_senha, registrado_nome, registrado_senha):
        if usuario_nome != registrado_nome:
            return False

        ph = PasswordHasher()
        
        # Usando async to run a blocking call (verify) in a non-blocking way
        try:
            # Verificação assíncrona da senha
            asyncio.to_thread(ph.verify, registrado_senha, usuario_senha)
            return True 
        except VerifyMismatchError:
            return False

    async def validar_login(self):
        return await self.separar_dados()

