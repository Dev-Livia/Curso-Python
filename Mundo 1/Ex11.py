#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

Largura =  float(input('Largura da parede: '))
Altura =  float(input('Altura da parede: '))
Area = Largura * Altura
tinta = Area / 2

print('''Sua parede tem a dimensão de {} x {} e sua área {}m
      Para pintar essa parede, você precisará de {}L de tinta '''.format(Largura, Altura, Area, tinta))