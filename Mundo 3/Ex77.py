#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('aprender', 'a', 'confiar',
            'no', 'processo', 'e',
            'essencial', 'para', 'seu',
            'crescimento')
for p in palavras:
    print(f' \n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')