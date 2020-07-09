num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
num3 = int(input('Digite um terceiro número: '))
# O exercicio no curso em video foi muito mais simplificado.

if num1>num2 and num1>num3 and num2>num3:
    print('Maior {}\nMenor {}'.format(num1, num3))
if num2>num3 and num2>num1 and num3>num1:
    print('Maior {}\nMenor {}'.format(num2, num1))
if num1>num2 and num1>num3 and num3>num2:
    print('Maior {}\nMenor {}'.format(num1, num2))
if num2>num3 and num2>num1 and num1>num3:
    print('Maior {}\nMenor {}'.format(num2, num3))
if num3>num2 and num3>num1 and num2>num1:
    print('Maior {}\nMenor {}'.format(num3, num1))
else:
    print('Maior {}\nMenor {}'.format(num3, num2))


