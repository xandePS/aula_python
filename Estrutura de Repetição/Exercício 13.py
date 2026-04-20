# Cálculo de potência (Base ^ Expoente) sem usar função pronta.

base = int(input("Base: "))
exp = int(input("Expoente: "))
potencia = 1
for _ in range(exp): potencia *= base
print(f"Resultado: {potencia}")