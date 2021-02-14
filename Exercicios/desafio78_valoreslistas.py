lista = []
for v in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
print('='*40)
print(f'Você digitou os valores: {lista}')
ma = max(lista)
mi = min(lista)
print(f'O maior valor digitado foi: {ma} nas posições ', end='')
for i, p in enumerate(lista):
    if p == ma:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {mi} nas posições ', end='')
for i, p in enumerate(lista):
    if p == mi:
        print(f'{i}...', end='')