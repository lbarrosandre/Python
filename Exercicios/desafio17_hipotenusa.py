import math
cco = int(input('Qual o comprimento do cateto oposto? '))
cca = int(input('Qual o comprimento do cateto adjacente? '))
hyp = math.hypot(cco, cca)
print('Hipotenusa é igual: {:.2f}'.format(hyp))



