# Verificação de data

data = input("Data (dd/mm/aaaa): ")
try:
    dia, mes, ano = map(int, data.split('/'))
    valida = False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31: 
            valida = True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30: 
            valida = True
    elif mes == 2:
        limite = 29 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else 28
        if 1 <= dia <= limite: valida = True
    print("Válida" if valida else "Inválida")
except:
    print("Formato inválido")