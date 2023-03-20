#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

N1 = float(input('Primeira nota: '))
N2 = float(input('Segunda nota: '))
Média = (N1 + N2) / 2

print('Sua média final é {:.1f} '.format(Média))

if Média < 5.0:
    print('Você foi REPROVADO')

elif Média > 5.0 and  Média < 6.9:
    print('Você está de RECUPERAÇÃO') 
else:
    Média > 7.0
    print('Você foi APROVADO')
