dados = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        dados[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{dados[l][c]:^5}] ', end='')
    print()