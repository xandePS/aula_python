# Sistema de Pedidos Lanchonete.

menu = {100: 1.2, 101: 1.3, 102: 1.5, 103: 1.2, 104: 1.3, 105: 1.0}
total_geral = 0
while True:
    cod_p = int(input("Código (0 para fechar): "))
    if cod_p == 0: break
    if cod_p in menu:
        q = int(input("Qtd: "))
        sub = menu[cod_p] * q
        total_geral += sub
        print(f"Subtotal: R$ {sub:.2f}")
print(f"Total Pedido: R$ {total_geral:.2f}")