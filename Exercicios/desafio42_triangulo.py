ret1 = int(input('Digite o valor da primeira reta: '))
ret2 = int(input('Digite o valor da segunda reta: '))
ret3 = int(input('Digite o valor da terceira reta: '))
a = abs(ret2 - ret3) < ret1 < ret2 + ret3
b = abs(ret1 - ret3) < ret2 < ret1 + ret3
c = abs(ret1 - ret2) < ret3 < ret1 + ret2
if a == b == c == True and ret1 == ret2 == ret3:
    print('É possivel formar um triângulo!!!\nEste triangulo será \033[1;33mEQUILATERO\033[m')
elif a == b == c == True and ret1 != ret2 != ret3 != ret1:
    print('É possivel formar uma triângulo!!!\nEste triangulo será \033[1;34mESCALENO\033[m')
elif a == b == c == True and ret1 == ret2 or ret1 == ret3 or ret2 == ret3:
    print('É possivel formar uma triângulo!!!\nEste triangulo será \033[1;35mISOSCELES\033[m')
else:
    print('Não possivel formar um Triângulo!')

