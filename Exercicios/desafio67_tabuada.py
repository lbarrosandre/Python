while True:
    tabuada = int(input('Quer ver a tabuada de qual número? '))
    if tabuada < 0:
        break
    for c in range (1, 11):
        print(f'{tabuada} x {c} = {tabuada*c}')
print('\033[1:34mTABUADA FINALIZADA')