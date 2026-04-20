# Média aritmética de N notas.

n_notas = int(input("Quantas notas? "))
print(f"Média: {sum(float(input('Nota: ')) for _ in range(n_notas))/n_notas}")