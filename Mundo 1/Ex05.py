#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

Num = int(input('Digite um número: '))
Antecessor = Num - 1 
Sucessor = Num + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(Num, Antecessor, Sucessor))