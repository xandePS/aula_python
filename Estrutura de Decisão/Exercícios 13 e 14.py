# Mensagem de saudação baseada no turno

turno = input("Informe seu turno (M-Matutino, V-Vespertino, N-Noturno): ").upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")