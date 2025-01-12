from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Criar uma instância do PasswordHasher
ph = PasswordHasher()

# Exemplo de senha
senha = "FWz>[[(>1.MN]fsN.H%~fVh{mELpQNj%dS_bJ6)a@zEgj0,PN(&*INg6d|O|^y[EwR>]#<*N&)s8;Q{1h-lSl2k]39y9{&S*bhK="

# 1. Gerar o hash da senha
hash_senha = ph.hash(senha)
print(f"Hash gerado: {hash_senha}")

# 2. Verificar se a senha corresponde ao hash
try:
    ph.verify(hash_senha, senha)
    print("Senha verificada com sucesso!")
except VerifyMismatchError:
    print("Senha incorreta!")
