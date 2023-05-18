#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
Velocidade = int(input('Qual a velocidade do carro? '))
if Velocidade <= 80:
    print('Boa Viagem!!')
else:
    multa = (Velocidade - 80) * 7
    print('MULTADO!,Você exedeu o limite permitido que é de 80Km/h')
    print('Você acabou passando á {} km e devera pagar {}'.format(Velocidade,multa ))
