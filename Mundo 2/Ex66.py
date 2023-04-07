#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
cont = 1
soma = 0
while cont:
    num = int(input('Digite um número (999 para para): '))
    cont += 1
    soma += num  
    if num == 999:
        break
    cont -= 1
soma -= 999 
print(f'O total de números digitados foi {cont} e a soma entre esses números é {soma}!!!')