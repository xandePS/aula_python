# Leia 5 números e informe o maior.

nums = [float(input(f"Número {i+1}: ")) for i in range(5)]
print(f"Maior: {max(nums)}")