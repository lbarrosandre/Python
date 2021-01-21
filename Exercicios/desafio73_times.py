tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('='*50)
print('Lista de times do Campeonato Brasileiro:', tabela)
print('='*50)
print('Os cinco primeiros são:', tabela[:5])
print('='*50)
print('Os quatro últimos são:', tabela[-4:])
print('='*50)
print('Times em ordem alfabética:', sorted(tabela))
print('='*50)
pos = tabela.index('Chapecoense')
print(f'A Chapecoense está na {pos+1}ª posição')


