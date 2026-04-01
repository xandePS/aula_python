# Calculo de multa por peso excedente

pesopeixe = float(input("Informe o peso (KG) dos peixes: "))
multa = 0

while (pesopeixe > 50):
    multa = multa + 4
    pesopeixe = pesopeixe - 1

print(f"O valor da multa é: {multa}")