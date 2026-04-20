# Caixa registradora rudimentar.

while True:
    print("Lojas Tabajara")
    total_compra, item = 0, 1
    while True:
        p_item = float(input(f"Produto {item}: R$ "))
        if p_item == 0: break
        total_compra += p_item
        item += 1
    print(f"Total: R$ {total_compra:.2f}")
    pago = float(input("Dinheiro: R$ "))
    print(f"Troco: R$ {pago - total_compra:.2f}\n")