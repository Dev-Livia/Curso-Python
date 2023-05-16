#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite o nome completo: ")

nomes = nome.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)