import random
x = random.randint(1, 10)
certo = int(input('Digite um numero de 1 a 10: '))
if certo == x:
    print('Parabéns!!! Você acertou o numero')
else:
    print('Você errou, tente outra vez!')