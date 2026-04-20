#  Leia 5 números e informe a soma e a média.

nums = [float(input(f"Número {i+1}: ")) for i in range(5)]
print(f"Soma: {sum(nums)} | Média: {sum(nums)/5}")