#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

N1 = float(input('Primeira nota: '))
N2 = float(input('Segunda nota: '))
Média = (N1 + N2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(N1, N2, Média))
if Média < 5.0:
    print('Aluno está REPROVADO')
elif Média < 6.9:
    print('Aluno está RECUPERAÇÃO')
else:
    print('Aluno está APROVADO')
  