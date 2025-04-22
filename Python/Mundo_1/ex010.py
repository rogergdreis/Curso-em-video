# Crie um programa que leia quanto dinheiro uma pessoa ter na carteira e mostre quantos Dólares ela pode comprar.

n = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, n/5.80))
