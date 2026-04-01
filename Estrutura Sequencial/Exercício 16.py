# Calculo de tinta por metro quadrado

area = float(input("Informe o tamanho da área a ser pintada (m²): "))

print ("A cobertura de tinta é de 1 litro para cada 3 metros quadrados")
print ("Lata de tinta: R$80,00 (18 litros)")

lata_tinta = 18 * 3
proporcao = area / lata_tinta

print(f"Voce precisará de {proporcao:.2f} latas de tinta")
