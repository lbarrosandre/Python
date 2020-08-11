from datetime import date
atual = date.today().year
t1 = 0
t2 = 0
for p in range(1, 8):
    n = int(input('Qual o ano de nascimento da Pessoa {}: '.format(p)))
    idade = atual - n
    if idade >= 21:
        t1 += 1
    else:
        t2 += 1
print('{} pessoas são maiores de idade.'.format(t1))
print('{} pessoas são menores de idade.'.format(t2))