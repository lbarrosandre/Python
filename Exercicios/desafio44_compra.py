preco = float(input('Preço do produto: R$ '))
print('Codição de Pagamento:\n1 - Dinheiro/Cheque\n2 - Cartão Debito\n3 - Cartão Credito até 2x\n4 - Cartão Credito 3x com juros')
pag = int(input('Opção: '))
if pag == 1:
    print('10% de desconto\nValor final: R$ {:.2f}'.format(preco*0.9))
elif pag == 2:
    print('5% de desconto\nValor final: R$ {:.2f}'.format(preco*0.95))
elif pag == 3:
    print('Preço sem desconto\nValor final: R$ {:.2f}'.format(preco))
elif pag == 4:
    print('Juros de 20%\nValor final: R$ {:.2f}'.format(preco*1.2))
else:
    print('>> Opção não existe <<')

