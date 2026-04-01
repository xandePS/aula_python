# Média de três notas parciais e status

notas3 = [float(input(f"Nota {i+1}: ")) for i in range(3)]
m3 = sum(notas3) / 3
if m3 == 10: 
    print(f"Aprovado com Distinção ({m3:.2f})")
elif m3 >= 7: 
    print(f"Aprovado ({m3:.2f})")
else: 
    print(f"Reprovado ({m3:.2f})")

