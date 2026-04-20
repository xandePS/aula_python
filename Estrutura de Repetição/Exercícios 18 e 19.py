# Menor, maior e soma de N números (entre 0 e 1000).

n_elementos = int(input("Quantidade de números: "))
conjunto = []
while len(conjunto) < n_elementos:
    val = float(input("Valor: "))
    if 0 <= val <= 1000: conjunto.append(val)
    else: print("Apenas entre 0 e 1000!")
print(f"Menor: {min(conjunto)} | Maior: {max(conjunto)} | Soma: {sum(conjunto)}")