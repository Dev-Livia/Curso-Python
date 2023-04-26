#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
Produtos = ('Água', 3.00,
            'Agua com gás', 4.00,
            'Lápis', 2.00,
            'Regua', 6.00,
            'Mochila', 55.00,
            'Apontador', 3.00,
            'Garrafa', 65.66 )
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range (0, len(Produtos)):
    if pos % 2 == 0:
        print(f'{Produtos[pos]:.<30}', end='')
    else:
        print(f'R${Produtos[pos]:>7.2f}')