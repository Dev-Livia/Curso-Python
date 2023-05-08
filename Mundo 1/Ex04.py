#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

al = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(al))
print('Só tem espaços? ', al.isspace())
print('é um número? ', al.isnumeric())
print('é alfabético? ', al.isalpha())
print('É alfanumérico? ', al.isalnum())
print('Está em maiúsculas? ', al.isupper())
print('Está em mínusculas?', al.islower())
print('Está captalizada? ', al.istitle())
