galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')

pessoas = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:]) ### Este simbolo é para criar uma copia de dados
    dado.clear()
print(pessoas)

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')