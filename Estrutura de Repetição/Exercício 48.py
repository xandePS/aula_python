# Competição de ginástica e Inversão de número.

nome_ginasta = input("Atleta: ")
notas = [float(input(f"Nota {i+1}: ")) for i in range(7)]
notas.sort()
media_ginasta = sum(notas[1:-1]) / 5
print(f"Melhor: {notas[-1]} | Pior: {notas[0]} | Média: {media_ginasta:.2f}")
