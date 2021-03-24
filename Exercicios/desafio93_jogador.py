dados = dict()
gols = []
co = 0

dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    co = co + 1
dados['gols'] = gols
dados['total'] = sum(gols)

print('-=-' * 30)
print(dados)
print('-=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 30)
print(f'O jogador {dados["nome"]} jogou {co} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c}, fez {dados["gols"][c]} goals.')
print(f'Foi um total de {dados["total"]} gols.')


