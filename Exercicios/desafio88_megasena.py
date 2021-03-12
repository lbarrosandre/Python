from random import sample
print('-------------------------')
print('    JOGO DA MEGA-SENA')
print('-------------------------')
jogos = []
jg = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'>>>>>> SORTEANDO {jg} JOGOS <<<<<<')
print()
for c in range(0, jg):
    jogos.append(sorted(sample(range(1, 61), 6)))
for c in range(0, jg):
    print(f'Jogo {c+1}: {jogos[c]}')
print('########### BOA SORTE ###########')