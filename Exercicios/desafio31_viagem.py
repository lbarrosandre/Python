viagem = float(input('Qual a distância da sua viagem em kilometros? '))
if viagem <= 200:
    print('O preço da passagem será de R$ {:.2f}'.format(viagem*0.5))
else:
    print('O preço da passagem será de R$ {:.2f}'.format(viagem*0.45))