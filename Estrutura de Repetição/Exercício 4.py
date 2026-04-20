# Cálculo de anos para população A ultrapassar B.

popA, taxaA = 80000, 0.03
popB, taxaB = 200000, 0.015
anos = 0

while popA < popB:
    popA *= (1 + taxaA)
    popB *= (1 + taxaB)
    anos += 1
print(f"Levará {anos} anos para a população A ultrapassar a B.")