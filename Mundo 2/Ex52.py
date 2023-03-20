# Aula 56 Analisador completo
SomaIdade = 0
MédiaIdade = 0
Homem = 0
NomeVelho = ''
totmulher20 = 0
for Pessoas in range(1, 5):

    print('----- {} PESSOA ----- '.format(Pessoas))
    Nome = str(input('Digite seu nome: ')).strip()
    Idade = int(input('Digite sua idade: '))
    Sexo = str(input('Sexo [F / M]? ')).strip()

    SomaIdade += Idade
    if Pessoas == 1 and Sexo in 'M':
        MaiorNome = Idade
        NomeVelho = Nome
    if Sexo in 'Mm' and Idade > Homem:
        Homem = Idade
        NomeVelho = Nome
    if Sexo in 'Ff' and Idade < 20:
        totmulher20 += 1
MédiaIdade = SomaIdade / 4
print('A média de idade do grupo é de {} anos'.format(MédiaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(Homem, NomeVelho))
print('Ao todo são {} Mulheres com menos de 20 anos '.format(totmulher20))