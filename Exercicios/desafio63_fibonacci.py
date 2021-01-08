s1 = 0
s2 = 1
print('='*22)
print('SEQUÊNCIA DE FIBONACCI')
print('='*22)
n = int(input('Quantos termos você mostrar: '))
print('~'*22)
print('{} -> {} '.format(s1, s2), end='')
c = 3
while c <= n:
    s3 = s2 + s1
    print('-> {} '.format(s3), end='')
    s1 = s2
    s2 = s3
    c += 1
print('-> FIM')

#Entendimento fácil, o mais complicado é qual o calculo que deve ser feito.
