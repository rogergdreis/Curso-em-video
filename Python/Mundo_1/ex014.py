# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em °C: '))

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(temp, (temp * 9/5) + 32))
