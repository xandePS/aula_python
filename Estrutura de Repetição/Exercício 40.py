#  Aluno mais alto e mais baixo entre dez conjuntos de dados.
maior_altura = 0
menor_altura = 500  # Valor inicial alto para comparação
aluno_mais_alto = 0
aluno_mais_baixo = 0

for _ in range(10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura (cm): "))
    
    if altura > maior_altura:
        maior_altura = altura
        aluno_mais_alto = numero
    if altura < menor_altura:
        menor_altura = altura
        aluno_mais_baixo = numero

print(f"Mais alto: Aluno {aluno_mais_alto} com {maior_altura}cm")
print(f"Mais baixo: Aluno {aluno_mais_baixo} com {menor_altura}cm")