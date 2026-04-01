# Caixa eletrônico: distribuição de notas (1, 5, 10, 50, 100).

saque = int(input("Valor do saque (10-600): "))
if 10 <= saque <= 600:
    for nota in [100, 50, 10, 5, 1]:
        qtd_notas = saque // nota
        saque %= nota
        if qtd_notas > 0: 
            print(f"{qtd_notas} nota(s) de R${nota}")
else:
    print("Valor fora do limite")