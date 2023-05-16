'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

Nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(Nome.upper()))
print('Seu nome em minúsculas é {}'.format(Nome.lower()))
print('O nome possui {}'.format(len(Nome) - Nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(Nome.find))

