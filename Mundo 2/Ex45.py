#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random

print("Bem-vindo ao Jokenpô!")
print("Escolha entre pedra, papel ou tesoura.")

opcoes = ["pedra", "papel", "tesoura"]

jogada_jogador = input("Sua jogada: ").lower()
jogada_computador = random.choice(opcoes)

print("Jogador:", jogada_jogador)
print("Computador:", jogada_computador)
print("-------------------")

if jogada_jogador == jogada_computador:
    print("Empate!")
elif jogada_jogador == "pedra":
    if jogada_computador == "papel":
        print("Computador venceu!")
    else:
        print("Jogador venceu!")
elif jogada_jogador == "papel":
    if jogada_computador == "tesoura":
        print("Computador venceu!")
    else:
        print("Jogador venceu!")
elif jogada_jogador == "tesoura":
    if jogada_computador == "pedra":
        print("Computador venceu!")
    else:
        print("Jogador venceu!")
else:
    print("Jogada inválida!")
