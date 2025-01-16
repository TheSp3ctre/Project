import jwt
import datetime

class CriandoJWT():
    def __init__(self, id_user: int, credencial_JWT: str,user):
        self.SECRET_KEY = credencial_JWT
        self.id = id_user
        self.user = user
    
    def _criando(self):
        payload = {
            "user_id": self.id,  # ID do usuário
            "username": self.user,  # Função do usuário
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiração do token
        }
        # Gerar o token
        token = jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")
        return token
