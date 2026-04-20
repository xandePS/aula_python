# Tabela de parcelamento de dívida com juros progressivos.

divida = float(input("Valor da dívida: "))
print("Valor Dívida | Valor Juros | Parcelas | Valor Parcela")

opcoes = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]
for parcelas, perc_juros in opcoes:
    juros = divida * (perc_juros / 100)
    total = divida + juros
    v_parcela = total / parcelas
    print(f"R$ {total:.2f} | R$ {juros:.2f} | {parcelas} | R$ {v_parcela:.2f}")