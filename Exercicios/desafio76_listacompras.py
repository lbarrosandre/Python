lista = ('Leite', 2.99, 'Frango', 16.90, 'Sorvete', 16.50, 'Iogurte', 4.79, 'Arroz', 12.35, 'Pão de forma', 4.70,
          'Bolo de fubá', 9.00, 'Cerveja', 1.89, 'Detergente', 1.29, 'Pasta de dente', 3.40, 'Desinfetante', 5.30,
          'Leite condensado', 4.15)
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
for n in range(0, len(lista)):
    if n % 2 == 0:
        print(f'{lista[n]:.<32}', end='')
    else:
        print(f'R$ {lista[n]:>5.2f}')
print('='*40)