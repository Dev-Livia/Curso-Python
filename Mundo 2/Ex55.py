#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
MaiorPeso = MenorPeso = 0
for c in range(1,6):
    Peso = float(input(f'Digite o {c}ª peso: '))
    if Peso > MaiorPeso:
        MaiorPeso = Peso
    else:
        Peso < MenorPeso
        MenorPeso = Peso
print('O maior peso é {:.2f}'.format(MaiorPeso))
print('O menor peso é {:.2f}'.format(MenorPeso))