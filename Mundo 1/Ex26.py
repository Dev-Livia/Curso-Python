#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ")

quantidade = frase.lower().count("a")
primeira_posicao = frase.lower().find("a")
ultima_posicao = frase.lower().rfind("a")

print("Quantidade de letras 'A':", quantidade)
print("Primeira ocorrência na posição:", primeira_posicao)
print("Última ocorrência na posição:", ultima_posicao)