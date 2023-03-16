#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

msg = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(msg))
print('Tem espaços? ', msg.isspace())
print('é um número? ', msg.isnumeric())
print('é alfabetico? ', msg.isalpha())
print('é alfanúmerico? ', msg.isalnum())
print('está em maiúsculas? ', msg.isupper())
print('Está em minusculas? ', msg.islower())
print('Está captalizada? ', msg.istitle())