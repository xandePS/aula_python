# Calculo da velocidade de download

arquivo_mbyte = float(input("Infome o tamanho do arquivo (MB): "))
internet = float(input("Informe a velocidade da internet (Mbps): "))

arquivo_mbit = arquivo_mbyte * 8
velocidade = arquivo_mbit/ internet
tempo_download = velocidade / 60

print(f"A velocidade de download é de {velocidade} MBs")
print(f"Vai demorar aproximadamente {tempo_download:.2f} minutos")