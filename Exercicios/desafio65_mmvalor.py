cont = 0
soma = 0
maior = 0
menor = 0
opc = ''
while opc != 'n':
        n = int(input('Digite um valor: '))
        opc = str(input('Quer digitar outro valor [S/N]? ')).lower().strip()
        cont += 1
        soma += n
        m = soma/cont
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('Você digitou {} valores e a média de todos os valores é igual a {:.2f}'.format(cont, m))
print(('O maior valor é {} e o menor valor é {}'.format(maior, menor)))

