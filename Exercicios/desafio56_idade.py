somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
tmulher20 = 0
for p in range(1, 5):
    print('===== {}º PESSOA ====='.format(p))
    n = str(input('Nome: '.format(p))).strip()
    i = int(input('Idade: '.format(p)))
    s = str(input('Sexo m/f: '.format(p))).strip()
    somaidade += i #Somar
    if p == 1 and s in 'Mm':
        maioridade = i
        nomevelho = n
    if s in 'Mm' and i > maioridade:
        maioridade = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        tmulher20 += 1 #Contar
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tmulher20))
