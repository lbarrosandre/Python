velocidade = int(input('Qual a velocidade do carro? '))
x = (velocidade - 80)*7
if velocidade > 80:
    print('Você excedeu a velocidade minima permitida de 80 km/h, você foi multado e pagará R${:.2f} de multa'.format(x))
else:
    print('Você está dentro da velocidade permitida!')