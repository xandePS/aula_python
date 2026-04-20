# Verificação de número primo e seus divisores.

p = int(input("Número para verificar se é primo: "))
divs = [i for i in range(1, p + 1) if p % i == 0]
if len(divs) == 2:
    print(f"{p} é primo.")
else:
    print(f"{p} não é primo. É divisível por: {divs}")