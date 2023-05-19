#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

A = float(input('Primeiro segmento: ')) 
B = float(input('Segundo segmento: ')) 
C = float(input('Terceiro segmento: ')) 

if A + B > C:
    A + C > B
    B + C > A
    print('Os segmentos acima PODEM formar triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')