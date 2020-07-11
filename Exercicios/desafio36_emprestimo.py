valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Salario base: R$ '))
anos = int(input('Pagar em quantos anos? '))
x = valor/(anos*12)
if x > salario*0.3:
    print('A prestação de R$ {:.2f} excedeu 30% so seu sálário \033[1;31m>> EMPRESTIMO NEGADO <<\033[m'.format(x))
elif x <= salario*0.3:
    print('\033[1;33m>>> EMPRESTIMO APROVADO <<<\033[m O valor da sua prestação é R$ {:.2f}'.format(x))