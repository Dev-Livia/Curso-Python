#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))

primo = True

# Verifica se o número é maior que 1
if numero > 1:
    # Percorre os números de 2 até o número - 1
    for i in range(2, numero):
        # Verifica se o número é divisível por algum valor do intervalo
        if numero % i == 0:
            primo = False
            break
else:
    primo = False

# Verifica se o número é primo ou não
if primo:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")