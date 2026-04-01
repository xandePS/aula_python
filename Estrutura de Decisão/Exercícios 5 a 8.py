# Leitura de duas notas e cálculo de média com status

print("Insira as notas do aluno")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado") 
else:
    print("Reprovado")