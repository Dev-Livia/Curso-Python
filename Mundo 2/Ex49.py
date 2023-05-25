#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
Num = int(input('Digite um número para ver sua tabuada: '))
for C in range(0,11):
    print('{} x {} = {}'.format(Num, C, Num * C))