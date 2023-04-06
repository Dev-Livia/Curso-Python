#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = Média = num = cn = cont = Maior = Menor = 0

while cn != 'N':
   num = int(input('Digite um Número: '))
   cn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
   cont += 1
   soma += num
   if cont == 1:
      Maior = Menor = num
   else:
      if num > Maior:
         Maior = num
      if num < Menor:
            Menor = num
Média = soma / cont
print('''Você digitou {} números e a média foi {:.2f} 
        O MENOR número foi {} e o MAIOR {}'''.format(cont, Média, Menor, Maior))

