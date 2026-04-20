# Competição de salto em distância (eliminando melhor e pior).

while True:
    nome = input("Atleta (vazio para sair): ")
    if not nome: break
    saltos = [float(input(f"{j+1}º Salto: ")) for j in range(5)]
    
    melhor, pior = max(saltos), min(saltos)
    saltos.remove(melhor)
    saltos.remove(pior)
    media_saltos = sum(saltos) / len(saltos)
    
    print(f"Melhor salto: {melhor}m | Pior salto: {pior}m")
    print(f"Resultado final: {nome}: {media_saltos:.1f} m\n")