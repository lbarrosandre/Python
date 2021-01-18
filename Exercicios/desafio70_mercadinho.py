totalp = mil = barato = c = 0
x = ' '
print('~'*40)
print('MERCADINHO BARATÃO')
print('~'*40)
while True:
    np = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$ '))
    print('='*40)
    opc = ' '
    while opc not in 'sn':
        opc = str(input('Quer Continuar? [S/N} ')).lower().strip()[0]
        print('-'*40)
    totalp += preco
    if preco > 1000:
        mil += 1
    c += 1
    if c == 1:
        barato = preco
    else:
        if preco < barato:
            barato = preco
            x = np


    if opc == 'n':
        break
print('='*40)
print(f'O total gasto foi de R$ {totalp}')
print(f'{mil} produtos custam mais de R$ 1000.00')
print(f'O Produto mais barato é o(a) {x} e custa R$ {barato}')

