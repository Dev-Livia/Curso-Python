#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for Pares in range(1,51):
    if Pares % 2 == 0 :
        print('{}'.format(Pares), end='.. ')
print('Acabou')