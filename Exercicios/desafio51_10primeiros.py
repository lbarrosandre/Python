a = int(input('Digite um número inicial: '))
b = int(input('Digite o valor da razão: '))
x = a + (10 - 1) * b
y = x + 1
z = x - 1
if b < 0:
    for c in range(a, z, b):
        print(c)
else:
    for c in range(a, y, b):
        print(c)
