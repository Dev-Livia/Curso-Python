#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato
Soma = Prod_Caro = Prod_Barato = 0
while True:
    Produto = str(input('Informe o nome do produto: '))
    Preço = float(input('Informe o preço do produto: R$ '))
    print('==' * 20)
    while True:
        Opç = str(input('Deseja continuar [S/N]: ')).upper()
        if Opç == 'S':
            break
        elif Opç == 'N':
            break
        else:
            print('Opção inválida. Por favor, escolha S ou N para sair')
    
    if Preço > Prod_Caro:
        Prod_Caro = Preço
    if Preço < Prod_Barato:
        Prod_Barato = Preço
    
    if Opç == 'N':
        break
    Soma += Preço

print('O Total do gasto é {:.2f}'.format(Soma))
print('O item de maior valor é de R$ {:.2f}'.format(Prod_Caro))
print('O item de menor valor é de R$ {:.2f}'.format(Prod_Barato))