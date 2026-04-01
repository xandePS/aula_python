# Programa que lê três números e mostre o maior e o menor deles

lista_nums = [float(input(f"Número {i+1}: "))for i in range(3)]
print(f"O maior número listado é: {max(lista_nums)}")
print(f"O menor número listado é: {min(lista_nums)}")