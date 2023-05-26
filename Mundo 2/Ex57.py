#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
Sexo = str(input('Informe seu sexo:[M/F] ')).strip().upper()[0]
while Sexo not in 'MmFf':
    Sexo = str(input('Dados inválidos. Por favor, tente novamente: '))
print('Sexo {} registrado com sucesso'.format(Sexo))