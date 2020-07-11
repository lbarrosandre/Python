ret1 = int(input('Digite o valor da primeira reta: '))
ret2 = int(input('Digite o valor da segunda reta: '))
ret3 = int(input('Digite o valor da terceira reta: '))
a = abs(ret2 - ret3) < ret1 < ret2 + ret3
b = abs(ret1 - ret3) < ret2 < ret1 + ret3
c = abs(ret1 - ret2) < ret3 < ret1 + ret2
if a == True and b == True and c == True:
    print('É possivel formar um triângulo!!!')
else:
    print('Não possivel!')


