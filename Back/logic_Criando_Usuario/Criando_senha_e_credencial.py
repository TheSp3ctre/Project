import random
import string
import os

class CriandoSenhaeCredencial():
    def __init__(self):
        self.senha = str
        self.credencial = str

    async def _criandoSenhaeCredencial(self):
        # Lista de caracteres permitidos, sem aspas e barras
        caracteres_permitidos = string.ascii_letters + string.digits + string.punctuation
        caracteres_permitidos = caracteres_permitidos.replace('"', "").replace("'", "").replace("\\", "").replace("/", "")

        # Gerando a senha e credencial
        self.senha = ''.join(random.choice(caracteres_permitidos) for i in range(50))
        self.credencial = ''.join(random.choice(caracteres_permitidos) for i in range(50))

        self._salvandoemtxt() # Posteriormente tirar esse metodo 
    
    def _armazenandoSenhaeCredencialParaUso(self):
        # Retornando as credenciais em uma lista
        return [self.senha, self.credencial]
    
    
    
    def _salvandoemtxt(self):
        relativePath = os.path.join('senha', 'senha.txt') # Lembrar de tirar esse metodo depois !

        with open (relativePath, 'w') as file:
            file.write(self.senha)

