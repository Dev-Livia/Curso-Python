'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

ProdutoCaro = ProdutoBarato = Total = c = 0
NomeProduBarato = ' '
while True:
    Produto = str(input('Nome do produto: '))
    Valor = float(input('Preço do produto: R$  '))
    c += 1
    Total += Valor
    if Valor > 1000:
        ProdutoCaro += 1
    if c == 1 or Valor < ProdutoBarato:
        ProdutoBarato = Valor
        NomeProduBarato = Produto
    opç = ' '
    while opç not in 'SN':  
        opç = str(input('Deseja Continuar [S/N]? ')).strip().upper()[0]
        print('----' * 15)  
    if opç == 'N':
        break
print('------ FIM DO PROGRAMA ------')
print(f'O gasto total dessa compra é R${Total:.2f}')
print(f'Temos {ProdutoCaro} produtos que custa mais de R$ 1.000 ')
print(f'O nome do produto mais barato é {NomeProduBarato} que custa R$ {ProdutoBarato:.2f}')