# Salário
# Adaptado por Neilor Tonin, URI  Brasil

# Timelimit: 1
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

id_funcionario = int(input())
num_horas_trabalhadas = int(input())
valor_hora_trabalhada = float(input())

salary = num_horas_trabalhadas * valor_hora_trabalhada

print("Number = " + str(id_funcionario))
print("SALARY = %.2f" % salary)