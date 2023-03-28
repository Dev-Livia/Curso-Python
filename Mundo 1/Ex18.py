#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
angulo = float(input('digite o ângulo que deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
coss = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,coss))
tan = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tan))