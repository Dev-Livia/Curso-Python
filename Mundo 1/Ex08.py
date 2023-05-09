#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Distancia em metrôs: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
m = valor * 10
centímetros = valor * 100
milímetros = valor * 1000

print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{} dm'.format(m))
print('{} cm'.format(centímetros))
print('{} mm'.format(milímetros))
