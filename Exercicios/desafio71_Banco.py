print('#'*40)
print('{:^40}'.format('SIMULAÇÃO CAIXA ELETRÔNICO'))
print('#'*40)
valor = int(input('Qual será o valor a ser retirado? R$ '))
print('='*40)
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*40)
print('Volte Sempre!!! Tenha um bom dia!')
