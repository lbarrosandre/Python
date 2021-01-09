n = 0
c = 0
s = 0
while n != 999:
    if c == 0:
        n = int(input('Digite um número: '))
        c += 1
        s += n
    else:
        n = int(input('Digite mais um número: '))
        c += 1
        s += n
print('Foram digitados {} números e a soma de todos os números é igual a {}'.format(c-1, s-999))