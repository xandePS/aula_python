# Média semestral com atribuição de conceitos (A, B, C, D, E).

nota_a = float(input("Insira a nota 1: "))
nota_b = float(input("Insira a nota 2: "))
m_final = (nota_a + nota_b) / 2

if 9 <= m_final <= 10: 
    conceito = "A"
elif 7.5 <= m_final < 9: 
    conceito = "B"
elif 6 <= m_final < 7.5: 
    conceito = "C"
elif 4 <= m_final < 6: 
    conceito = "D"
else: 
    conceito = "E"


if conceito in "ABC":
    status = "APROVADO"  
else: 
    status = "REPROVADO"

print(f"Média: {m_final} | Conceito: {conceito} | {status}")