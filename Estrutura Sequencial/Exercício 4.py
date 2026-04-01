# Calcular média do aluno no ano

nota1 = float(input("Informe a nota do primeiro bimeste: "));
nota2 = float(input("Informe a nota do segundo bimeste: "));
nota3 = float(input("Informe a nota do terceiro bimeste: "));
nota4 = float(input("Informe a nota do quarto bimeste: "));

media = (nota1 + nota2 + nota3 + nota4) / 4;

print(f"A média do aluno é: {media}");