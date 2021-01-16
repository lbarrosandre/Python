import random
c = 0
print('='*23)
print('>> JOGO PAR OU ÍMPAR <<')
print('='*23)
while True:
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).lower().strip()[0]
    print('='*23)
    comp = random.randint(1, 10)
    total = valor + comp
    if total % 2 == 0:
        print(f'Você jogou {valor} e o computador jogou {comp}. Total de {total} deu PAR')
        print('-'*23)
        if escolha == 'p':
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!!!')
            break
    elif total % 2 != 0:
        print(f'Você jogou {valor} e o computador jogou {comp}. Total de {total} deu ÍMPAR')
        print('-'*23)
        if escolha == 'i':
            print('Você VENCEU!!!')
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!!!')
            break
    c += 1
print(f'GAME OVER!!! Você venceu {c} vezes.')