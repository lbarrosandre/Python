c1 = c2 = 0
exp = input('Digite uma expressão qualquer: ')
for n in exp:
    if n == '(':
        c1 += 1
    elif n == ')':
        c2 += 1
if c1 == c2:
    print('Sua Expressão está correta!')
else:
    print('Sua expressão está errada!')