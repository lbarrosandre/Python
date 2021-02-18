print("######## CALCULAR MEDIA NOTAS ########\n")
nota1 = float(input("Qual o valor da sua 1º prova? "))
nota2 = float(input("Qual o valor da sua 2º prova? "))
nota3 = float(input("Qual o valor da sua 3º prova? "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Você foi aprovado, sua média foi de: ",media)
elif (media < 7 and media >= 6):
    print("Você esta de recuperação, sua média foi de: ",media)
else:
    print("Você foi reprovado, sua média foi de: ",media)



