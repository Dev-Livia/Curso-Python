#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

Produto = float(input('Qual o valor do produto? R$ '))
Desconto = Produto - (Produto * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto vai custar R${:.2f}'.format(Produto, Desconto))