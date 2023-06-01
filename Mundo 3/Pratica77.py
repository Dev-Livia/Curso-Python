#Exercício fornecido pelo ChatGPT
Palavras = ('A', 'Luz', 'Brilha','Nas','Trevas', 'e', 'As', 'Trevas', 'Não', 'a', 'Derrotaram')
vogais = ['a', 'e', 'i','o','u']

for palavra in Palavras:
    Vogais_Palavras = []
    for letra in palavra:
        if letra.lower() in vogais:
            Vogais_Palavras.append(letra)
    quantidade_vogais = sum(palavra.lower().count(vogal) for vogal in vogais)
    print(f'Palavra: {palavra} | Possui {quantidade_vogais} vogais')



