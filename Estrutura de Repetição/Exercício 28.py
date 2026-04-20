# Valor médio gasto em coleção de CDs.

qtd_cds = int(input("Qtd CDs: "))
investido = sum(float(input("Valor do CD: ")) for _ in range(qtd_cds))
print(f"Total: R${investido:.2f} | Média por CD: R${investido/qtd_cds:.2f}")