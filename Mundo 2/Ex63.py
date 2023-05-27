#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input("Digite o número de elementos da Sequência de Fibonacci que você deseja exibir: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    proximo_elemento = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_elemento)

# Exibe os elementos da Sequência de Fibonacci
for elemento in fibonacci:
    print(elemento, end=" ")

print()  # Pula uma linha após exibir os elementos
