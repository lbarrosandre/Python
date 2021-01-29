dados = ('Carro', 'Bicicleta', 'Motocicleta', 'Casa', 'Terra',
         'Caixa', 'Igreja', 'Boneco', 'Campo', 'Cozinha',
          'Criança', 'Mesa', 'Cortina')
for n in dados:
    print(f'\nNa palavra {n.upper()} temos: ', end='')
    for l in n:
        if l.lower() in 'aeiou':
            print(f'{l}', end=' ')





