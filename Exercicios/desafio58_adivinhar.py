import random
x = 1
c = random.randint(1, 10)
a = int(input('Tente adivinhar, digite um valor: '))
while a != c:
    a = int(input('Você não adivinhou, tente novamente: '))
    x += 1
print('Você acertou com {} tentativa(s)!!!'.format(x))


