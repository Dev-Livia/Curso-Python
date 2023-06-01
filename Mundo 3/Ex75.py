#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
numeros = tuple(int(input('Digite um número: ')) for _ in range(4))

# Contagem do valor 9
contagem_9 = numeros.count(9)
print(f'O valor 9 apareceu {contagem_9} vezes.')

# Posição do primeiro valor 3
if 3 in numeros:
    posicao_3 = numeros.index(3) + 1  # Adiciona 1 para exibir a posição correta
    print(f'O primeiro valor 3 foi digitado na posição {posicao_3}.')
else:
    print('O valor 3 não foi digitado.')

# Números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print(f'Os números pares digitados foram: {", ".join(map(str, numeros_pares))}.')

