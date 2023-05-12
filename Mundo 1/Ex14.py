#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Tempreatura = float(input('Informe a temperatura: '))
Conversão = (Tempreatura * 9 / 5) + 32 
print('A temperatura de {}C° corresponde a {}°F'.format(Tempreatura, Conversão))
