#  Eleição com três candidatos.

votos = {1: 0, 2: 0, 3: 0}
eleitores = int(input("Nº Eleitores: "))
for _ in range(eleitores):
    v = int(input("Voto (1, 2 ou 3): "))
    if v in votos: votos[v] += 1
print(f"Resultado: {votos}")