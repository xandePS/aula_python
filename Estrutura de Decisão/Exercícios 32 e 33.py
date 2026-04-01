# Preços de frutas com desconto por volume ou valor total

kg_mor = float(input("Kg Morango: "))
kg_mac = float(input("Kg Maçã: "))

if kg_mor <= 5:
    preco_mor = 2.50 
else:
    preco_mor = 2.20

if kg_mac <= 5:
    preco_mac = 1.80  
else:
    preco_mac = 1.50
    
total_kg = kg_mor + kg_mac

total_pagar = (kg_mor * preco_mor) + (kg_mac * preco_mac)

if total_kg > 8 or total_pagar > 25:
    total_pagar *= 0.90
print(f"Total a pagar: R${total_pagar:.2f}")