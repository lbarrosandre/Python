frase = str(input('Digite uma frase: ')).lower().strip()
l = frase.count('a')
p = frase.find('a')+1
up = frase.rfind('a')+1
print('A letra A aparece {} vezes\nA primeira posicação é {}\nA ultima posição é {}'.format(l, p, up))

