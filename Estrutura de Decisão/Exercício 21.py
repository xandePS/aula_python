# Cálculo de raízes de equação do segundo grau

import math

a = float(input("Valor de a: "))
if a == 0:
    print("Não é equação do 2º grau.")
else:
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("Não possui raízes reais.")
    elif delta == 0:
        print(f"Uma raiz real: {-b / (2 * a)}")
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes: {r1} e {r2}")