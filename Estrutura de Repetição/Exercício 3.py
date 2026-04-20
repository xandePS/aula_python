# Validação de Nome, Idade, Salário, Sexo e Estado Civil.

while True:
    nome = input("Nome (maior que 3 caracteres): ")
    if len(nome) > 3: break

while True:
    idade = int(input("Idade (0-150): "))
    if 0 <= idade <= 150: break

while True:
    salario = float(input("Salário (maior que 0): "))
    if salario > 0: break

while True:
    sexo = input("Sexo (f/m): ").lower()
    if sexo in ['f', 'm']: break

while True:
    estado_civil = input("Estado Civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']: break