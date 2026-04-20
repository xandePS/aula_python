# Cálculo de fatorial com formatação.

num_f = int(input("\nFatorial de: "))
fatorial = 1
print(f"{num_f}! =", end=" ")
for i in range(num_f, 0, -1):
    fatorial *= i
    print(f"{i}", end=" . " if i > 1 else f" = {fatorial}\n")