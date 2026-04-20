# Média de alunos por turma (máx 40).

turmas = int(input("Qtd turmas: "))
total_alunos = 0
for i in range(turmas):
    while True:
        qtd = int(input(f"Alunos na turma {i+1}: "))
        if qtd <= 40: break
        print("Máximo 40!")
    total_alunos += qtd
print(f"Média: {total_alunos/turmas:.2f}")