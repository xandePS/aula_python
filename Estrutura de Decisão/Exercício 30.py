# Classificação de participação em crime através de 5 perguntas.

perguntas = ["Telefonou para a vitima?", "Esteve no local do crime?",\
 "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
pontos = sum(1 for p in perguntas if input(f"{p} (s/n): ").lower() == 's')

if pontos == 2: 
    status_crime = "Suspeita"
elif 3 <= pontos <= 4: 
    status_crime = "Cúmplice"
elif pontos == 5: 
    status_crime = "Assassino"
else: 
    status_crime = "Inocente"
print(f"Classificação: {status_crime}")