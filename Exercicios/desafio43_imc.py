peso = float(input('Qual o seu peso (KG): '))
altura = float(input('Qual a sua altura (m): '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, Abaixo do Peso'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.2f}, Peso Ideal'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.2f}, Sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.2f}, Obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f}, Obesidade Morbida'.format(imc))