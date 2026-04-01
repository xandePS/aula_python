# Informe se o número é inteiro ou decimal

numero = float(input("Número: "))
if numero == round(numero):
    print("Inteiro")
else:
    print("Decimal")
