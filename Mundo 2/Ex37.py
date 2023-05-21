#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
Num = int(input('Digite um numero inteiro: '))
print('''[ 1 ] converter para BINÁRIO
        [ 2 ] converter para OCTAL
        [ 3 ] converter para HEXADECIMAL ''')
Opcao = int(input('Sua opção: '))
if Opcao == 1:
    Binario = bin(Num)
    print('{} convertido para BINÁRIO é igual a {}'.format(Num, Binario))
elif Opcao == 2:
    Octal = oct(Num)
    print('{} convertido para OCTAL é igual a {}'.format(Num, Octal))
elif Opcao == 3:
    Hexa = hex(Num)
    print('{} convertido para OCTAL é igual a {}'.format(Num, Hexa))
else:
    print('Opção inválida. tente novamente!')