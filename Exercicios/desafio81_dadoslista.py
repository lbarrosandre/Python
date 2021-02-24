lista = []
while True:
    v = lista.append(int(input('Digie um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('='*40)
print(f'Foram digitados {len(lista)} números!')
a = lista
a.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {a}')
if 5 in a:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

