# Faça um algoritimo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario,salario*1.15))
