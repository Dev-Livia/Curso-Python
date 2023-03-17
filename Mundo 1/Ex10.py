#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

print('Observação: R$ 1 Dólar americano atualmente está valendo  R$ 5 Real brasileiro')

Br = float(input('Quanto dinheiro você possui: R$  '))
Dólar = Br / 5
print('Você possui R$ {} reais, ao converter você terá R$ {:.2f} '.format(Br, Dólar))