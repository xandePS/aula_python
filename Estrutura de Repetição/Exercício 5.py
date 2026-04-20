# Versão do exercício 04 com entradas do usuário e repetição.

while True:
    pA = int(input("População A: "))
    tA = float(input("Taxa A (%): ")) / 100
    pB = int(input("População B: "))
    tB = float(input("Taxa B (%): ")) / 100
    a = 0
    while pA < pB:
        pA *= (1 + tA)
        pB *= (1 + tB)
        a += 1
    print(f"Anos: {a}")
    if input("Repetir? (s/n): ").lower() != 's': break