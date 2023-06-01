#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Palavras = ('Ate', 'Aqui', 'o', 'Senhor', 'Nos', 'Ajudou')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in Palavras:
    vogais_na_palavra = []  # Lista para armazenar as vogais encontradas em cada palavra
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_na_palavra.append(letra)
    print(f'Palavra: {palavra} | Vogais: {", ".join(vogais_na_palavra)}')