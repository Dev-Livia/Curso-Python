#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
Lista = []
Menor =  None
Maior = 0
for C in range(1,6):
    Num = int(input('Digite um número: '))
    Lista.append(Num)
    if Menor is None or Num < Menor:
        Menor = Num
        Posição_Menor = Lista.index(Menor)
    if Num > Maior:
        Maior = Num
        Posição_Maior = Lista.index(Maior)
print(f' O menor número é: {Menor} na posição {Posição_Menor}')
print('===' * 30)
print(f'O maior número é: {Maior} na posição {Posição_Maior}')

