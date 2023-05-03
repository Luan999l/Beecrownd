#  beecrowd | 1017
# Gasto de Combustível

# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1 
tempo = int(input())
velocidade = int(input())

combustivel = 12

litros = tempo * velocidade / combustivel

print('{:.3f}'.format(litros))