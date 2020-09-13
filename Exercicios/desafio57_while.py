sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado invalido!!! Favor digitar a informação correta: ')).strip().upper()[0]
print('Sexo {} informado corretamente'.format(sexo))

