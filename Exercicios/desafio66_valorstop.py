c = s = 0
while True:
    n = int(input('Digite um valor (999 para paras): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é igual a {s}')