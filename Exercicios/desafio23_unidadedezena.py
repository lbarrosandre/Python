numero = int(input('Digite um número entre 0 e 9999: '))
u = numero % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u,d,c,m))


