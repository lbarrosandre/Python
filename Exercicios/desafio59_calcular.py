from time import sleep
opc = 0
maior = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
while opc != 5:
    print('######### > MENU < #########')
    print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')
    opc = int(input('\nDigite a opção: '))
    if opc == 1:
        print('A Soma de {} + {} é igual a: {}\n'.format(n1, n2, n1+n2))
    elif opc == 2:
        print('A multiplicação de {} x {} é igual a: {}\n'.format(n1, n2, n1*n2))
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}'.format(maior))
    elif opc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opc == 5:
        print('Finalisando ...')
    else:
        print('Informação inválida!!! Digite novamente.')
    print('=-='*15)
    sleep(2)
print('\n\033[1:33mPROGRAMA FINALIZADO!!!')




