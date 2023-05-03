# beecrowd | 1010
# Cálculo Simples
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

lista = input().split(" ")
cod1 = int((lista[0]))
n1 = int((lista[1]))
valor1 = float((lista[2]))

lista = input().split(" ")

cod2 = int((lista[0]))
n2 = int((lista[1]))
valor2 = float((lista[2]))

total = n1 * valor1 + n2 * valor2
print(str("VALOR A PAGAR: R$ ") + str("{:0.2f}".format(total)))