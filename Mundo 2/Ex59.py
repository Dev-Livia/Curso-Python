#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

Maior = 0
while True:
    P1 = int(input('Informe o primeiro valor: '))
    P2 = int(input('Informe o segundo valor: '))
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    Opç = int(input('Qual é a sua opção? '))
    print('==' * 20)
    if Opç == 1:
        print(' {} + {} = {}'.format(P1, P2, P1 + P2))
    elif Opç == 2:
        print('{} x {} = {}'.format(P1, P2, P1 * P2))
    elif Opç == 3:
        Maior = max(P1, P2)
        print('O maior número é {}'.format(Maior))
    elif Opç == 4:
        continue
    else:
        break
print('Saindo do programa')