num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
quest = int(input('Digite um número de 0 a 20: '))
while quest > 20 or quest < 0:
      quest = int(input('Tente novamente! Digite um número de 0 a 20: '))
print('Você digitou o número', num[quest])

