#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

Num = int(input('Digite um número: '))

print('O dobro de {} vale {}'.format(Num,(Num * 2)))
print('O triplo de {} vale {}'.format(Num,(Num * 3)))
print('A raiz quadrada de {} vale {:.2f}'.format(Num,(Num ** (1/2))))
