from datetime import date
data = int(input('Digite o ano de nascimento: '))
x = date.today().year - data
if x < 10:
    print('Sua categoria é: MIRIM')
elif x < 15:
    print('Sua categoria é: INFANTIL')
elif x < 20:
    print('Sua categoria é: JUNIOR')
elif x < 21:
    print('Sua categoria é: SENIOR')
else:
    print('Sua categoria é: MASTER')