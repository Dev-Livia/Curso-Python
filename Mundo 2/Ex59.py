'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
Num = int(input('Digite o primeiro valor: '))
Num1 = int(input('Digite o segundo valor: '))
Opção = 0
while Opção != 5:
    print(''' 
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa
     ''')
    Opção = int(input('>>> Qual sua Opção:   '))
    if Opção == 1:
        print('A soma entre {} + {} = {}'.format(Num, Num1, (Num + Num1)))
    elif Opção == 2:
        print('A multiplicação entre {} x {} = {} '.format(Num, Num1, (Num * Num1) ))
    elif Opção == 3:
        if Num > Num1:
           maior = Num
        else: Num1 > Num
        maior = Num1
        print('Entre {} e {} o maior valor é {}'.format(Num, Num1, maior))
    elif Opção == 4:
        print('Informe os números novamente: ')
        Num = int(input('Primeiro valor: '))
        Num1 = int(input('Segundo valor: '))
    elif Opção == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente Novamente')
    print('=-=' * 10)  
print('Fim do programa')