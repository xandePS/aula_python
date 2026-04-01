# Realize operação e informe se o resultado é par/ímpar, +/- e int/dec. 

v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
op = input("Operação (+, -, *, /): ")
res_op = eval(f"{v1} {op} {v2}")
info_pi = "Par" if res_op % 2 == 0 else "Ímpar"
info_pn = "Positivo" if res_op >= 0 else "Negativo"
info_id = "Inteiro" if res_op == round(res_op) else "Decimal"
print(f"Resultado: {res_op} | {info_pi}, {info_pn}, {info_id}")