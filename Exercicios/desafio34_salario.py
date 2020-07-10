salario = float(input('Digite o valor do seu sálario: '))
if salario > 1250:
    print('Seu aumento foi de 10% e seu novo salário é R$ {:.2f}'.format(salario*1.1))
else:
    print('Seu aumento foi de 15% e seu novo salário é R$ {:.2f}'.format(salario * 1.15))