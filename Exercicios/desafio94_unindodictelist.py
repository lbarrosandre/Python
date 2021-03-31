dados = dict()
grupo = list()
c = 0
s = 0

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] '))
        if dados['sexo'] in 'MmFf':
            break
        else:
            print("ERRO! Por favor, digite apenas M ou F.")
    dados['idade'] = int(input('Idade: '))
    c += 1
    s = dados['idade'] + s
    while True:
        resp = input('Quer Continuar? [S/N]: ')
        if resp in 'NnSs':
            break
        else:
            print("ERRO! Responda apenas S ou N.")
    grupo.append(dados.copy())
    if resp in 'Nn':
        break

media = s/c
print(grupo)
print("=-" *30)
print(f"A) Ao todo temos {c} pessoas cadastradas.")
print(f"B) A média de idade é de {media:5.2f} anos.")
print('C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}  ', end='')
print()
print('D) Lista das pessoas que estão acima da média:', end='')
for p in grupo:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v} ', end="")
print()
print('>> ENCERRADO <<')
