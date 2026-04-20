# Eleição presidencial (votos nominais, nulos e brancos).

votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_votos = 0
while True:
    v = int(input("Voto (1-4 candidatos, 5-Nulo, 6-Branco, 0-Fim): "))
    if v == 0: break
    if v in votos:
        votos[v] += 1
        total_votos += 1

for k in range(1, 5):
    print(f"Candidato {k}: {votos[k]} votos")
print(f"Nulos: {votos[5]} | Brancos: {votos[6]}")
if total_votos > 0:
    print(f"% Nulos: {(votos[5]/total_votos)*100:.2f}%")
    print(f"% Brancos: {(votos[6]/total_votos)*100:.2f}%")