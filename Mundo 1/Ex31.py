#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

Distancia = int(input('Qual a distância da viagem? '))

if Distancia <= 200:
    Tarifa = Distancia * 0.50
    print('Você está prestes a começar uma viagem de {}'.format(Distancia))
    print('E o preço da sua passagem será R$ {:.2f}'.format(Tarifa))
else:
    Tarifa = Distancia * 0.45
    print('Você está prestes a começar uma viagem de {}'.format(Distancia))
    print('E o preço da sua passagem será R$ {:.2f}'.format(Tarifa))