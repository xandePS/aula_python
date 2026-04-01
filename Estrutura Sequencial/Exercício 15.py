# Calculo de salário liquido

salario_hora = float(input("Quanto você ganha por hora: "))
horas = float(input("Quantas horas trabalhou no mês: "))

salario_bruto = salario_hora * horas

ir = salario_bruto * 0.11

inss = salario_bruto * 0.08

sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f"Salário Bruto: {salario_bruto}")
print(f"Desconto do INSS (8%): {inss}")
print(f"Desconto do Imposto de Renda (11%): {ir}")
print(f"Desconto do sindicato (5%): {sindicato}")
print(f"Salário Liquido: {salario_liquido}")



