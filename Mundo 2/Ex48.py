#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0

for numero in range(1, 501,2):
    if numero % 3 == 0:
        soma += numero
        contador += 1

print('A soma dos números múltiplos de 3 no intervalo de 1 a 500 é:', soma)
print('A quantidade de números divisíveis por 3 no intervalo de 1 a 500 é:', contador)
