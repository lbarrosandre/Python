import math
s = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        s += c
print('A soma de todos os números impares de 1 a 500 divisores por 3 é: {}'.format(s))
