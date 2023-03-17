#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Preço = float(input('Qual o preço do produto: R$ '))
Desconto = (Preço - (Preço * 5 / 100))
print('O produto custava R$ {}, após ser aplicado o desconto de 5% Passou a ser {:.2f}'.format(Preço, Desconto))