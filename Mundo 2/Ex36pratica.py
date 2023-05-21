# Empréstimo Bancário

Casa = float(input('Qual o valor da casa que pretende comprar?R$ '))
Salario_Comprador = float(input('Qual o total da sua renda?R$ '))
Anos = int(input('Em quantos anos pretende pagar? '))
Prestacao_mensal = Casa / (Anos * 12)

if Prestacao_mensal <= Salario_Comprador * 0.3:
    print('O emprestimo foi APROVADO e você pagará {:.2f} mensalmente'.format(Prestacao_mensal))
else:
    print('Emprestimo NEGADO')