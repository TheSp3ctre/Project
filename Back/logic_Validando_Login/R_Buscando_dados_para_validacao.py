import asyncmy

class BuscandoCredenciaisNoDataBase:
    def __init__(self, nome_do_usuario):
        self.nome_do_usuario = str(nome_do_usuario)
    
    async def buscar_credenciais(self):
        try:
            # Conectando-se ao banco de dados de maneira assíncrona
            async with asyncmy.connect(
                user="root",
                password="root",
                host="localhost",
                port=3306,
                database="localhost"
            ) as conexao:
                async with conexao.cursor() as cursor:
                    # Consulta SQL para buscar dados do usuário
                    await cursor.execute("""
                        SELECT id, nome, senha, credencial_JWT
                        FROM usuarios
                        WHERE nome = %s
                    """, (self.nome_do_usuario,))
                    
                    # Obtendo o resultado da consulta
                    resultado_da_busca = await cursor.fetchone()

                    if resultado_da_busca is not None:
                        lista_de_dados_encontrados = {
                            "id": resultado_da_busca[0],
                            "nome": resultado_da_busca[1],  
                            "senha": resultado_da_busca[2],
                            "credencial_JWT": resultado_da_busca[3],
                        }
                        return lista_de_dados_encontrados
                    else:
                        # Retorna um aviso caso o usuário não seja encontrado
                        return False

        except asyncmy.MySQLError as e:
            # Tratando e retornando o erro de forma explícita no log
            return {"erro": f"Erro no banco de dados: {e}"}



    
    