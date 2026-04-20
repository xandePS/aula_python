# Sistema de correção de provas com gabarito.

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas_turma = []
while True:
    acertos = 0
    for i in range(10):
        resp = input(f"Resposta questão {i+1}: ").upper()
        if resp == gabarito[i]: acertos += 1
    notas_turma.append(acertos)
    if input("Outro aluno vai usar o sistema? (s/n): ").lower() != 's': break

print(f"Maior acerto: {max(notas_turma)} | Menor acerto: {min(notas_turma)}")
print(f"Total alunos: {len(notas_turma)} | Média da Turma: {sum(notas_turma)/len(notas_turma)}")