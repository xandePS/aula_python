import math
# Loja de tintas com latas e galões e folga de 10%

area_complexa = float(input("Informe a área a ser pintada (m²): "))
litros_com_folga = (area_complexa / 6) * 1.1

# Situação 1: Apenas latas de 18L (R$ 80)
apenas_latas = math.ceil(litros_com_folga / 18)
custo_apenas_latas = apenas_latas * 80

# Situação 2: Apenas galões de 3,6L (R$ 25)
apenas_galoes = math.ceil(litros_com_folga / 3.6)
custo_apenas_galoes = apenas_galoes * 25

# Situação 3: Mistura (menor desperdício
mistura_latas = int(litros_com_folga // 18)
resto = litros_com_folga % 18
mistura_galoes = math.ceil(resto / 3.6)
custo_mistura = (mistura_latas * 80) + (mistura_galoes * 25)

print(f"Apenas latas: {apenas_latas} (R$ {custo_apenas_latas:.2f})")
print(f"Apenas galões: {apenas_galoes} (R$ {custo_apenas_galoes:.2f})")
print(f"Mistura: {mistura_latas} latas e {mistura_galoes} galões (R$ {custo_mistura:.2f})")