a = int(input('Digite um número: '))
b = int(input('Digite o valor da Razão: '))
c = 0
x = a
total = 0
t = 10
while t != 0:
    total += t
    while c < total:
        print('{} '.format(x), end='')
        x = x + b
        c += 1
    print('PAUSA')
    t = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))







