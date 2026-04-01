# Verificação de tipo de triângulo

lado_a = float(input("Lado A: "))
lado_b = float(input("Lado B: "))
lado_c = float(input("Lado C: "))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    if (lado_a == lado_b == lado_c): 
        tipo = "Equilátero"
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c): 
        tipo = "Isósceles"
    else: 
        tipo = "Escaleno"
    print(f"Triângulo {tipo}")
else:
    print("Não formam um triângulo")