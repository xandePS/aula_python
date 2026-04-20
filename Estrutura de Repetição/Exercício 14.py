# Contador de pares e ímpares em 10 números inteiros.

dez_nums = [int(input(f"N{i+1}: ")) for i in range(10)]
pares = sum(1 for x in dez_nums if x % 2 == 0)
print(f"Pares: {pares} | Ímpares: {10 - pares}")