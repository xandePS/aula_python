# Nota entre zero e dez com validação.

while True:
    nota = float(input("Digite uma nota (0-10): "))
    if 0 <= nota <= 10:
        break
    print("Valor inválido! Tente novamente.")