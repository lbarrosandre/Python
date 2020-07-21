import random
from time import sleep
lista = ['PAPEL', 'PEDRA', 'TESOURA']
x = random.choice(lista)
escolha = str(input('Escolha uma opção: Pedra, Papel ou Tesoura? ')).upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if x == 'PEDRA' and escolha == 'PAPEL':
    print('Você: {}\nComputador: {}\nVocê Ganhou do Computador'.format(escolha, x))
elif x == 'TESOURA' and escolha == 'PEDRA':
    print('Você: {}\nComputador: {}\nVocê Ganhou do Computador'.format(escolha, x))
elif x == 'PAPEL' and escolha == 'TESOURA':
    print('Você: {}\nComputador: {}\nVocê Ganhou do Computador'.format(escolha, x))
elif x == escolha:
    print('Você: {}\nComputador: {}\nEmpate, Jogar Novamente!'.format(escolha, x))
else:
    print('Você: {}\nComputador: {}\n>> Você perdeu!!! <<'.format(escolha, x))





