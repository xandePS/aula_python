# Senso da Academia (Alto, Baixo, Gordo, Magro).

clientes = []
while True:
    cod = int(input("Código (0 para sair): "))
    if cod == 0: break
    clientes.append({'c': cod, 'a': float(input("Altura: ")), 'p': float(input("Peso: "))})