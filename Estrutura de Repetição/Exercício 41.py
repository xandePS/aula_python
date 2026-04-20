# Estatística de acidentes de trânsito em cinco cidades.

cidades = []
for i in range(5):
    cod = int(input(f"Código da cidade {i+1}: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))
    cidades.append({'cod': cod, 'vei': veiculos, 'aci': acidentes})

indices = [c['aci'] for c in cidades]
print(f"Maior índice: {max(indices)} | Menor índice: {min(indices)}")

media_veiculos = sum(c['vei'] for c in cidades) / 5
cidades_pequenas = [c['aci'] for c in cidades if c['vei'] < 2000]
media_acid_pequenas = sum(cidades_pequenas) / len(cidades_pequenas) if cidades_pequenas else 0

print(f"Média veículos: {media_veiculos} | Média acidentes (<2000 veículos): {media_acid_pequenas}")