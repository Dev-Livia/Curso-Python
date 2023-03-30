#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
total = 0
TERMOS = 10
while TERMOS != 0:
    total = total + TERMOS
    while cont <= total: 
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    TERMOS = int(input('Quantos termos você quer mostrar? '))
print('Progressão finalizada com {} termos'.format(total))

