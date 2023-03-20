Sexo = str(input('Informe seu sexo: [M / F] ')).strip().upper()[0]
while Sexo not in 'MmFf':
    Sexo = str(input('Por fovor informe o sexo novamente: [M / F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(Sexo))

