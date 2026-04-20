#  Série de Fibonacci até o valor ser maior que 500.

a, b = 0, 1
while a <= 500:
    print(a, end=" ")
    a, b = b, a + b
print(a) # Mostra o primeiro maior que 500