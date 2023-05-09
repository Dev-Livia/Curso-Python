#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

Nota1 = float(input('Primeira Nota: '))
Nota2 = float(input('Segunda Nota: '))
Média =  (Nota1 + Nota2) / 2

print('A primeira nota foi {} e a segunda {}'.format(Nota1, Nota2))
print('A média desse aluno foi {:.2f}'.format(Média))