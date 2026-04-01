#Cálculo de folha de pagamento com descontos

v_hora = float(input("Valor da hora: "))
q_horas = float(input("Horas trabalhadas: "))
bruto = v_hora * q_horas

if bruto <= 900:
    percentual_ir = 0
elif bruto <= 1500:
    percentual_ir = 5
elif bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

ir = bruto * (percentual_ir / 100)
inss = bruto * 0.10
fgts = bruto * 0.11
total_desc = ir + inss
liquido = bruto - total_desc

print(f"Bruto: R${bruto:.2f}")
print(f"IR({percentual_ir}%): R${ir:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"FGTS: R${fgts:.2f}")
print(f"Líquido: R${liquido:.2f}")
