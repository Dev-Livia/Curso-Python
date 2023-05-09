#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Real = float(input('Quanto deseja Converter? R$ '))
Dolar = Real / 5

print('Ao converter R$ {}'.format(Real))
print('Você terá US$ {}'.format(Dolar))