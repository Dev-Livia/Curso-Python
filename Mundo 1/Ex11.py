#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m.'.format(largura, altura, área))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))