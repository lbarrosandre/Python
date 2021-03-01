grupo = list()
pessoas = list()
maior = menor = cont = 0
nome1 = nome2 = ''

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    grupo.append(pessoas[:])
    pessoas.clear()
    resp = input('Quer Continuar? [S/N]: ')
    cont += 1
    for p in grupo:
        if cont == 1:
            maior = menor = p[1]
        else:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor:
                menor = p[1]
    if resp in 'Nn':
        break

print(f'Ao todo, você cadastrou {cont} pessoas!')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in grupo:
    if maior == p[1]:
        print(f'{p[0]} ',end='')
print()
print(f'O menor peso foi de {menor}Kg Peso de ',end='')
for p in grupo:
    if menor == p[1]:
        print(f'{p[0]} ',end='')