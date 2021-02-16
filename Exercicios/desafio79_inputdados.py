lista = []
while True:
    l = int(input('Digite um valor: '))
    if l not in lista:
        lista.append(l)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor em duplicidade. este valor não será considerado...')
    r = str(input('Quer continuar: [S/N] '))
    if r in 'Nn':
        break
print('Você digitou os valores:', sorted(set(lista)))
