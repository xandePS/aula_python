# Verificação se uma letra digitada é "F" ou "M" e imprima o sexo correspondente

sexo = input("Digite F para Feminino ou M para Masculino: ").upper()
if sexo == 'F':
    print("F - Feminino")
elif sexo == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido")