#  beecrowd | 1044
# Múltiplos

# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1 

a, b = map(int, input().split())

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a == b:
    print('Sao Multiplos')