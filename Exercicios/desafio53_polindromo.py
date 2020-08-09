frase = str(input('Digite uma palavra ou uma frase: ')).lower()
frase = ''.join(frase.split())
frase2 = frase[::-1]
if frase == frase2:
    print('Esta palavra ou frase >> É UM POLINDROMO')
else:
    print('Esta frase >> NÃO É UM POLINDROMO')
