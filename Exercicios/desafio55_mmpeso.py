#lista = []
#for p in range(1, 6):
  #  peso = float(input('Digite o peso da Pessoa {}: '.format(p)))
 #   lista.append(peso)
#print(max(lista))
#print(min(lista))

#############################################################################
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da Pesssoa {}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))
