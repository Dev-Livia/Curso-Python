#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Número = int(input('Digite um número: '))

milhar = Número // 1000
centena = (Número // 100) % 10
dezena = (Número // 10) % 10
unidade = Número % 10

print("Milhar:", milhar)
print("Centena:", centena)
print("Dezena:", dezena)
print("Unidade:", unidade)