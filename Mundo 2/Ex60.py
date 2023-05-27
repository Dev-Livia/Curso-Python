#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input("Digite um número: "))
fatorial = 1
contador = 1

if num < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    while contador <= num:
        fatorial *= contador
        contador += 1

    print("O fatorial de {} é {}.".format(num, fatorial))
