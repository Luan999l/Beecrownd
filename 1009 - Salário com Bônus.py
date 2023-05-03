# Salário com Bônus
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.


idfuncionario = input()
salaryFixo = float(input())
totalVendasMes = float(input())

total = totalVendasMes * 0.15

salaryFixo += total

print("TOTAL = R$ %.2f" % salaryFixo)
