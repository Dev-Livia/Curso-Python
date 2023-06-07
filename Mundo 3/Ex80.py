#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for _ in range(5):
    valor = int(input("Digite um valor numérico: "))
    if len(lista) == 0 or valor > lista[-1]:
        lista.append(valor)  # Adiciona no final da lista se for maior que o último elemento
    else:
        index = 0
        while valor > lista[index]:
            index += 1
        lista.insert(index, valor)  # Insere na posição correta

print("Lista ordenada:", lista)