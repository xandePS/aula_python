# Contagem de números por intervalos [0-25, 26-50, 51-75, 76-100].

intervalos = [0, 0, 0, 0] # [0-25], [26-50], [51-75], [76-100]
while True:
    n = float(input("Digite um número (negativo para sair): "))
    if n < 0: break
    if 0 <= n <= 25: intervalos[0] += 1
    elif 26 <= n <= 50: intervalos[1] += 1
    elif 51 <= n <= 75: intervalos[2] += 1
    elif 76 <= n <= 100: intervalos[3] += 1

print(f"0-25: {intervalos[0]} | 26-50: {intervalos[1]} | 51-75: {intervalos[2]} | 76-100: {intervalos[3]}")