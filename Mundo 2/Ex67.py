#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    nu = int(input('Digite um número para ver sua tabuada: '))
    if nu < 0:
            break
    for One in range(0, 11):
        mult = nu * One
        print(f'{One} X {nu} {mult}')
print('O programa foi ENCERRADO')