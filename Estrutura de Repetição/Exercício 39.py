# Aumento salarial anual (percentual dobra).

salario = float(input("Salário inicial: "))
percentual = 0.015
for ano in range(1996, 2026): # Exemplo até hoje
    salario *= (1 + percentual)
    percentual *= 2
print(f"Salário atual: R$ {salario:.2f}")