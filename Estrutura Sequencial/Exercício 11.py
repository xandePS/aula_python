# Numeros inteiros e reais

numeroint1 = int(input("Informe um numero inteiro: "))
numeroint2 = int(input("Informe outro numero inteiro: "))

numeroreal = float(input("Informe um numero real: "))

a = (numeroint1 * 2) + (numeroint2/2)

print(f"O produto do dobro do primeiro com a metade do segundo: {a}")

b = (numeroint1 * 3) + numeroreal

print(f"A soma do triplo do primeiro com o terceiro: {b}")

c = numeroreal **3

print(f"O terceiro elevado ao cubo: {c}")