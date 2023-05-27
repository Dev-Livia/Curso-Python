#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número inteiro (999 para parar): "))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1

print("Foram digitados {} números.".format(contador))
print("A soma entre eles é {}.".format(soma))
