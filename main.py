#  beecrowd | 1064
# Positivos e Média

# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1 

soma = 0
quantidade = 0
for i in range(6):
  valor = float(input())
  if valor > 0:
      soma = soma + valor
      quantidade = quantidade + 1

print(f"{quantidade} valores positivos")
print(f"{soma/quantidade : 0.1f}")





