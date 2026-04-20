# Mostrar n termos da série S = 1/1 + 2/3 + 3/5 + ...
n_s = int(input("Termos: "))
s, m = 0, 1
for i in range(1, n_s + 1):
    s += i / m
    print(f"{i}/{m}", end=" + " if i < n_s else "")
    m += 2
print(f"\nSoma: {s:.2f}")

# Cálculo de H com N termos: H = 1 + 1/2 + 1/3 ...
nh = int(input("Termos de H: "))
h_val = sum(1/i for i in range(1, nh + 1))
print(f"H = {h_val:.2f}")