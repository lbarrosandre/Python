import math
angulo = float(input('Digite um angulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno é {:.2f}\nO Cosseno é {:.2f}\ne a tangente é {:.2f}'.format(sen, cos, tan))
