#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
cont = soma = 0
for Num in range(1,7):
    Número = int(input('Digite um número: '))
    if Número % 2 == 0:
        cont += 1
        soma += Número
print('O total de números pares digitados foi {}'.format(cont))
print('E a soma entre esses números é {}'.format(soma))