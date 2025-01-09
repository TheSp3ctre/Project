from argon2 import PasswordHasher
import asyncio

class EncriptandoSenhaeCredencial():
    
    def __init__(self, senha, credencial):
        self.ph = PasswordHasher()
        self.senha = str(senha) 
        self.credencial = str(credencial)
        
        self.hash_senha = str
        self.hash_credencial = str
    
    async def _criandoHashsenhaEcredencial(self):
        # Usando asyncio.to_thread para rodar o processo de hashing em uma thread separada
        self.hash_senha = await asyncio.to_thread(self.ph.hash, self.senha)

        self.hash_credencial = await asyncio.to_thread(self.ph.hash, self.credencial)
    
    def _armazenandoSenhaEcredencialhashsParaUso(self):
        return [self.senha, self.hash_credencial]



        
