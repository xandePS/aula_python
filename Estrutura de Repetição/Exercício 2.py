# Criação de usuário e senha (não podem ser iguais).

while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if senha != usuario:
        break
    print("Erro: a senha não pode ser igual ao nome de usuário.")