n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='') #aqueles numeros que forem igual a zero, pintar de outra cor.
        tot += 1 #Este não entendi muito bem.
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'.format(n, tot))
if tot == 2:
    print('Portanto o número >> É PRIMO')
else:
    print('Portanto o número >> NÃO É PRIMO')

