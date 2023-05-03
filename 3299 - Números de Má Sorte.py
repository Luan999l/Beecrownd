#  beecrowd | 3299
# Números Má Sorte Pequenos

# Por Tomas Peiretti, UTN - FRSF AR Argentina
# Timelimit: 1

# Um número número 3 é de má sorte si contém um 1 seguido por um 3 entre seus dígitos. Por exemplo, o número 341329 é de má sorte, enquanto o número 26771 não é.

# Dado um inteiro N, seu programa terá que determinar se N é azarado ou não.

n = int(input())

n = str(n)
msg = 'NO es de Mala Suerte'
for i in range(0, len(n)):
    if n[i] == '1' and i != len(n) - 1:
        if n[i + 1] == '3':
            msg = 'es de Mala Suerte'
            break

print(n, msg)


