# Exibição do dia correspondente da semana .

dias = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}
dia_num = int(input("Número do dia (1-7): "))
print(dias.get(dia_num, "Valor inválido"))