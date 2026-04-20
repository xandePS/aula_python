# Mostre todos os primos entre 1 e N e o número de divisões.

limite_p = int(input("Primos até onde? "))
total_divisoes = 0
for num in range(2, limite_p + 1):
    e_primo = True
    for i in range(2, int(num**0.5) + 1):
        total_divisoes += 1
        if num % i == 0:
            e_primo = False
            break
    if e_primo: print(num, end=" ")
print(f"\nDivisões executadas: {total_divisoes}")