#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

N1 = int(input('Digite um número: '))
N2 = int(input('Digite mais um número: '))
N3 = int(input('Digite o ultimo número: '))

Menor = N1
if N2<N1 and N2<N3:
    Menor = N2 
if N3<N1 and N3 < N2:
    Menor = N3
#Verificando o Maior número 
Maior = N1
if N2>N1 and N2>N3:
    Maior = N2
if N3>N2 and N3>N1:
    Maior = N3
print('O MENOR número é {}'.format(Menor))
print('O MAIOR número é {}'.format(Maior))
