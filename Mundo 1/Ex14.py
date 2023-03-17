#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
C = float(input('Informe a temperatura em ºC: '))
F = 9 * C / 5 + 32
print('A temperatura de {} ºC corresponde a {} ºF'.format(C, F))
