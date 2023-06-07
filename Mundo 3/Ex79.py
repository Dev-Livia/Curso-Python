#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

Lista = []
while True:
    Num = int(input('Informe um valor: '))
    if Num in Lista:
        print('Valor Duplicado! não vou adicionar !!')
    else:
        Lista.append(Num)
        print('Valor inserido com sucesso !!')
    while True:
        Opç = str(input('Deseja continuar [S/N]? ')).upper()
        if Opç == 'S' or Opç == 'N':
            break
        else:
            print('Opção inválida. Digite S para continuar ou N para sair.')

    if Opç == 'N':
        break
Cresc = sorted(Lista)
print(f'Você digitou os valores: {Cresc}')