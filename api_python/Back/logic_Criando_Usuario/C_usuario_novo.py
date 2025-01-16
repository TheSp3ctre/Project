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
                database="frantello"
            ) as conexao:  # A conexão será fechada automaticamente após o bloco 'async with'
                async with conexao.cursor() as cursor:  # O cursor será fechado automaticamente após o bloco 'async with'
                    await cursor.execute("SELECT * FROM users WHERE nome = %s ",self.nome)
                    user_created = await cursor.fetchone()
                    if (user_created):
                        return {"message": "Esse usuário já está registrado.","status":False}
                    await cursor.execute("INSERT INTO users (nome,senha,credencial_JWT) VALUES (%s,%s,%s) ",(
                        self.nome,self.senha,self.credencial
                    ))
                    await cursor.execute('SELECT * FROM users WHERE nome = %s ',self.nome)
                    new_user = await cursor.fetchone()
                    await conexao.commit()
                    return {"message": "Usuário criado com sucesso","new_user":new_user,"status":True}
        except asyncmy.errors.OperationalError as e: 
            print(f'Erro ao executa database {e}')
            return {"message": "Ocorreu um erro no banco de dados","status":500}


