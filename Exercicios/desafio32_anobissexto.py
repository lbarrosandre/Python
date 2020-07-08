ano = int(input('Digite um ano: '))
# Neste exercicio foi feito mais um import de pacote chamado: datetime
# O exercicio ficou mais simplificado
# Este está bugado, ex. ano 1976
primeiro = ano%4==0
segundo = ano%100==0
terceiro = ano%400==0
if primeiro ==True and segundo ==False and terceiro ==False:
    print('O ano é >> \033[1;33mBISSEXTO\033[m <<')
elif primeiro ==True and segundo ==True and terceiro ==True:
    print('O ano é >> \033[1;33mBISSEXTO\033[m <<')
else:
    print('O ano ## \033[1;31mNÃO É BISSEXTO\033[m ##')