#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

Produtos =  (('Lápis', '1.75'),
            ('Borracha', '2.00'),
            ('Estojo','15.00'),
            ('Transferidor','25.00'),
            ('Compasso','9.99'),
            ('Mochila','120.00'),
            ('Caneta','22.30'),
            ('Livro','34.90'))
for Item, Preço in Produtos:
    print(f"{Item}: ........... R${Preço}")