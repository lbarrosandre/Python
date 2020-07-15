from  datetime import date
###### ALISTAMENTO ######
ano = int(input('Em que ano você nasceu? '))
x = date.today().year - ano
if x < 18:
    print('Você ainda vai se alistar, faltam {} anos'.format(18-x))
elif x > 18:
    print('Já passou o tempo de alistamento, você deveria ter alistado a {} anos atrás'.format(x-18))
else:
    print('É hora de se alistar')
