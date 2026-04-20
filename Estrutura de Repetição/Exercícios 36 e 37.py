# Tabuada com início e fim personalizados.

t_num = int(input("Tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))
if fim < inicio:
    print("Erro: fim menor que início.")
else:
    for i in range(inicio, fim + 1):
        print(f"{t_num} X {i} = {t_num * i}")