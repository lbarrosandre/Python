n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('Media é {}\n\033[1;31mREPROVADO'.format(media))
elif media >= 7.0:
    print('Media é {}\n\033[1;32mAPROVADO'.format(media))
else:
    print('Media é {}\n\033[1;36mRECUPERAÇÃO'.format(media))
