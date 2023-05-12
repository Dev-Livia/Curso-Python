#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

CatetoOposto = float(input('Digite o valor do cateto oposto: '))
CatetoAdjacente = float(input('Digite o valor do Cateto Adjacente: '))

Hipotenusa = (CatetoOposto**2 + CatetoAdjacente**2)

print('A hipotenusa vai medir {:.2f}'.format(sqrt(Hipotenusa)))
