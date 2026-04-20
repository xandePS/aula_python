# Menor, maior e média de temperaturas.

temps = []
while True:
    t = input("Temp (ou 'fim'): ")
    if t.lower() == 'fim': break
    temps.append(float(t))
print(f"Min: {min(temps)} | Max: {max(temps)} | Média: {sum(temps)/len(temps)}")