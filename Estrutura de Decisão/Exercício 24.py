# Quantidade de centenas, dezenas e unidades de um número menor que 1000

num_int = int(input("Digite um número < 1000: "))
centenas = num_int // 100
dezenas = (num_int % 100) // 10
unidades = num_int % 10
res = []

if centenas > 0: 
    res.append(f"{centenas} centena" + ("s" if centenas > 1 else ""))
if dezenas > 0: 
    res.append(f"{dezenas} dezena" + ("s" if dezenas > 1 else ""))
if unidades > 0: 
    res.append(f"{unidades} unidade" + ("s" if unidades > 1 else ""))
    
print(", ".join(res[:-1]) + (" e " if len(res) > 1 else "") + res[-1] if res else "Zero")