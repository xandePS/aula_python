# Listagem em ordem decrescente 

lista_nums = [float(input(f"Número {i+1}: "))for i in range(3)]
lista_nums.sort(reverse=True)
print(f"Listagem dos numeros em ordem decrescente: {lista_nums}")