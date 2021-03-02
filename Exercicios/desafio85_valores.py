dados = [[], []]

for p in range(1, 8):
    valor = int(input(f'Digite o {p}º valor: '))
    if valor % 2 == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)

print(f'Os valores pares digitados foram: {sorted(dados[0])}')
print(f'Os valores ímpares digitados foram: {sorted(dados[1])}')