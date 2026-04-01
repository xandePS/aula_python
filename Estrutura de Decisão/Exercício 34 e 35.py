# Promoção de carnes com cupom fiscal e desconto no cartão Tabajara
t_carne = int(input("Tipo: "))
qtd_carne = float(input("Kg: "))

cartao = input("Cartão Tabajara? (s/n): ").lower()
precos_carnes = {1: (4.9, 5.8), 2: (5.9, 6.8), 3: (6.9, 7.8)}
nomes_carnes = {1: "Filé Duplo", 2: "Alcatra", 3: "Picanha"}

p_un = precos_carnes[t_carne][0] if qtd_carne <= 5 else precos_carnes[t_carne][1]
total_bruto = qtd_carne * p_un
desc_cartao = total_bruto * 0.05 if cartao == 's' else 0

print(f"\n--- CUPOM FISCAL ---")
print(f"Tipo: {nomes_carnes[t_carne]} | Qtd: {qtd_carne}kg")
print(f"Bruto: R${total_bruto:.2f} | Desc: R${desc_cartao:.2f} | Final: R${(total_bruto - desc_cartao):.2f}")