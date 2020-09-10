altura = float(input('Digite a sua altura (m): '))
sexo = input('Digite seu sexo[M/F]: ')

if sexo == 'M':
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print(f'O peso ideal é: {peso}')