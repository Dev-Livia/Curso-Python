#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase: ").replace(" ", "").lower()

inverso = frase[::-1]

if frase == inverso:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
