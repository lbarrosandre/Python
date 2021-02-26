lista = []
lp = []
li = []
while True:
    v = lista.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('=-='*30)
print(f'A lista completa é: {lista}')
for n in lista:
    if n % 2 == 0:
        v = lp.append(n)
    else:
        v = li.append(n)

print(f'A lista de pares é:{lp}')
print(f'A lista de ímpares é:{li}')
