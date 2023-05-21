#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

Valor_Casa = float(input('Qual o valor da casa que pretende comprar:R$ '))
Salario = float(input('Quanto é seu salário?R$ '))
Anos = int(input('Em quantos anos deseja pagar? '))

Prestação_Mensal = Valor_Casa / (Anos * 12)

if Prestação_Mensal <= Salario * 0.3:
      print("Empréstimo aprovado! O valor da prestação mensal será de R$ {:.2f}".format(Prestação_Mensal))
else:
    print("Empréstimo negado. O valor da prestação excede 30% do salário.")