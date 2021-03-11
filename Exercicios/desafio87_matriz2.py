dados = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        dados[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('>'*80)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{dados[l][c]:^5}] ', end='')
    print()

print('>'*80)
soma = soma2 = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        if dados[l][c] % 2 == 0:
            soma += dados[l][c]
    soma2 += dados[l][2]
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma2}.')

for l in range(0, 3):
    for c in range(0, 3):
        if dados[1][c] == 0:
            maior = dados[1][c]
        else:
            if dados[1][c] > maior:
                maior = dados[1][c]

print(f'O maior valor da segunda linha é {maior}.')