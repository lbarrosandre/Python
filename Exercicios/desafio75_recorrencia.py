x = 0
a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))
c = int(input('Digite o 3º valor: '))
d = int(input('Digite o 4º valor: '))
dados = (a, b, c, d)
print(f'Os valores digitados foram: {dados}')
print(f'O número 9 apareceu {dados.count(9)} vezes.')
if 3 in dados:
    print(f'O número 3 apareceu pela primeira vez na posição {dados.index(3) + 1}.')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados são: ', end='')
for x in dados:
    if x % 2 == 0:
        print(x, end=' ')









