#  beecrowd | 1020
# Idade em Dias

# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1 


n = int(input())

a = n // 365
n = n - a*365

m = n // 30
n = n - m*30

d = n

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))
