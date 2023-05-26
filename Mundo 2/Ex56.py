##Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
Hom_Velho = ''
ContMulher = 0
Soma = 0

for pessoas in range(1, 5):
    print(f'{pessoas}ª')
    Nome = str(input('Nome: '))
    Idade = int(input('Informe a idade: '))
    Sexo = str(input('Sexo [F/M]: '))
    print('=' * 10)
    
    # Verificando qual o nome do homem mais velho
    if Sexo.upper() == 'M' and Idade > Hom_Velho:
        Hom_Velho = Nome
    
    # Verificando a média de idade do grupo
    Soma += Idade

    # Verificando quantas mulheres têm menos de 20 anos
    if Sexo.upper() == 'F' and Idade < 20:
        ContMulher += 1

Média = Soma / 4

print('O nome do homem mais velho é {}'.format(Hom_Velho))
print('A média de idade do grupo é de {}'.format(Média))
print('O total de mulheres com menos de 20 anos é de: {}'.format(ContMulher))
