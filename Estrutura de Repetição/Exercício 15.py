# Série de Fibonacci até o n-ésimo termo.

n_fib = int(input("Quantos termos de Fibonacci? "))
a, b = 1, 1
for _ in range(n_fib):
    print(a, end=" ")
    a, b = b, a + b