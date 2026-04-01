# Cálculo de valor de combustível com descontos progressivos

litros = float(input("Litros: "))
tipo = input("Tipo (A-álcool, G-gasolina): ").upper()

if tipo == 'A':
    p_litro = 1.90 
    desc = (0.03 if litros <= 20 else 0.05)
else:
    p_litro = 2.50
    desc = (0.04 if litros <= 20 else 0.06)
print(f"Total: R${(litros * p_litro * (1 - desc)):.2f}")