# Média de idade da turma (Jovem, Adulta, Idosa).

n_idades = int(input("Total de pessoas: "))
media_id = sum(int(input("Idade: ")) for _ in range(n_idades)) / n_idades
if media_id <= 25: status = "Jovem"
elif media_id <= 60: status = "Adulta"
else: status = "Idosa"
print(f"A turma é {status}.")