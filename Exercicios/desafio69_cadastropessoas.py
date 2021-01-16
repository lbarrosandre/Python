c = i = m = f = 0
print('='*41)
print('>>>>>>>>>> CADASTRO DE PESSOAS <<<<<<<<<<')
print('='*41)
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [F/M]: ')).strip().lower()[0]
        print('-'*41)
    if sexo == 'm':
        m += 1
    if sexo == 'f' and idade < 20:
        f += 1
    if idade >= 18:
        i += 1
    opc = ' '
    c += 1
    while opc not in 'sn':
        opc = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if opc == 'n':
        break
print('='*41)
print(f'Foram cadastradas {c} pessoas!')
print(f'{i} pessoas tem mais de 18 anos')
print(f'Foram cadastradas {m} homens ')
print(f'Foram cadastradas {f} mulheres com menos de 20 anos')