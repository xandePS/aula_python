# Tabelas de Preços (Artigos e Pães).

preco_un = float(input("Preço unitário do produto: "))
for i in range(1, 51):
    print(f"{i} - R$ {i * preco_un:.2f}")