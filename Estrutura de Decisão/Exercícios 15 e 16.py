# Cálculo de reajuste salarial

sal_atual = float(input("Digite o salário atual: "))
if sal_atual <= 280:
    percentual = 20
elif sal_atual <= 700:
    percentual = 15
elif sal_atual <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = sal_atual * (percentual / 100)
novo_sal = sal_atual + aumento

print(f"Antes: R${sal_atual:.2f}")
print(f"Reajuste: {percentual}%")
print(f"Aumento: R${aumento:.2f}")
print(f"Novo: R${novo_sal:.2f}")

