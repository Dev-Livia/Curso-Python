#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Tempreatura = float(input('Informe a temperatura: '))
Conversão = 32 + (Tempreatura * 9 / 5)
print('A temperatura de {}C° corresponde a {}°F'.format(Tempreatura, Conversão))
