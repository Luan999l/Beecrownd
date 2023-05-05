#  beecrowd | 1046
# Tempo de Jogo

# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1 



# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
# Entrada

# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
# Saída

# Apresente a duração do jogo conforme exemplo abaixo.



x = input().split()
i, f = x

i = int(x[0])
f = int(x[1])

if i < f:
    t = f - i
else:
    t = (24 - i) + f
print('O JOGO DUROU {} HORA(S)'.format(t))



