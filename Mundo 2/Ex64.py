#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
cont = 0
soma = 0
n = int(input('Digite um número [Digite 999 para parar]: '))
while n != 999:    
    n = int(input('Digite um número [Digite 999 para parar]: '))
    soma += n
    cont += 1
print('Você digitou {} Números e a soma entre eles foi {}'.format(cont, soma))