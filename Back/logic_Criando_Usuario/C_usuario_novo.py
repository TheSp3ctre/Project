import asyncmy

class CreateNovoUsuario():
    
    def __init__(self, nome, senha, credencial):
        self.nome = str(nome)
        self.senha = str(senha)
        self.credencial = str(credencial)
    
    async def _inserindoDadosnoBD(self):
        try:
            # Usando 'async with' para gerenciar a conexão e o cursor automaticamente
            async with asyncmy.connect(
                user="root",
                password="root",
                host="localhost",
                port=3306,
                database="localhost"
            ) as conexao:  # A conexão será fechada automaticamente após o bloco 'async with'
                async with conexao.cursor() as cursor:  # O cursor será fechado automaticamente após o bloco 'async with'
                    await cursor.execute(
                        "INSERT INTO usuarios (nome, senha, credencial_JWT) VALUES (%s, %s, %s)", 
                        (self.nome, self.senha, self.credencial)
                    )
                    await conexao.commit()
                    return True
        except asyncmy.MySQLError as e:
            return False


