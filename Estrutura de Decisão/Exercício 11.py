# Comparação de preço de três produtos e informe qual o mais barato para comprar
 
p1 = float(input("Preço produto 1: "))
p2 = float(input("Preço produto 2: "))
p3 = float(input("Preço produto 3: "))
if p1 < p2 and p1 < p3:
    print("Compre o primeiro produto.")
elif p2 < p3:
    print("Compre o segundo produto.")
else:
    print("Compre o terceiro produto.")