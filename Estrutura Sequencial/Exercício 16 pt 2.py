# Calculo de tinta por metro quadrado

area = float(input("Informe o tamanho da área a ser pintada (m²): "))

print ("A cobertura de tinta é de 1 litro para cada 6 metros quadrados")
print ("Lata de tinta: R$80,00 (18 litros)")
print ("Lata de tinta: R$25,00 (3.6 litros)")

lata_tinta = 18 * 6
proporcao = round(area / lata_tinta,2)

preco_lata = proporcao * 80

print(f"Voce precisará de {proporcao} latas de tinta: R${preco_lata}")

galao_tinta = 3.6 * 6
proporcao = round(area / galao_tinta,2)

preco_galao = proporcao * 25

print(f"ou voce precisará de {proporcao} galões de tinta: R${preco_galao}")