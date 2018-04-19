
#Funçao Exercicio 1
def ex1():
    print("Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.")

    num = float(input("Digite um numero: "))

    if(num > 0):
        print("Positivo")

    elif(num < 0):
        print("Negativo")

    elif(num == 0):
        print("Zero")

#Funçao Exercicio 2
def ex2():
    print("2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.")

    num = int(input("Digite um número: "))

    if((num % 2) == 0):
        print("Numero é par")

    else:
        print("Numero é impar")

#Funçao exercicio 3
def ex3():
    print("3) Faça um algoritmo que leia três números e imprima o maior.")

    num  = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    num3 = float(input("Digite mais um número: "))

    if(num > num2 and num > num3):
        print(num,"é maior")

    if(num2 > num and num2 > num3):
        print(num2,"é maior")

    if(num3 > num and num3 > num2):
        print(num3,"é maior")

#Funçao exercicio 4
def ex4():
    print("4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.")

    idade = int(input("Digite a sua idade: "))

    if(idade >= 18):
        print("Você já é de maior.")

    else:
        print("Você ainda não é de maior.")

#Funçao exercicio 5
def ex5():
    print("5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.")

    idadeFilho = int(input("Digite a sua Idade: "))
    idadeMae = int(input("Digite a idade da sua mãe: "))

    print("Quando você nasceu sua mãe tinha %i anos" %(idadeMae - idadeFilho))

#Funcao exercicio 6
def ex6():
    print("6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição).")

    print(50 * "-")

#Funçao exercicio 7
def ex7():
    print("7) Faça um algoritmo que peça um número ao usuário e verifique se o mesmo é par ou então ímpar.")

    num = int(input("Digite um número: "))

    if((num % 2) == 0):
        print("Numero é par")

    else:
        print("Numero é impar")

#Funçao exercicio 8
def ex8():
    print("8) Faça um algoritmo que peça três números. Primeiro, imprima o maior e, em seguida, o menor.")

    num = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    num3 = float(input("Digite um terceiro numero: "))

    if(num > num2 and num > num3):
        print(num, "é Maior")
        if(num2 < num3):
            print(num2, "é menor")
        else:
            print(num3, "é menor")

    if(num2 > num and num2 > num3):
        print(num2, "é maior")
        if(num < num3):
            print(num, "é menor")
        else:
            print(num3, "é menor")

    if(num3 > num and num3 > num2):
        print(num3,"é maior")
        if(num < num2):
            print(num, "é menor")
        else:
            print(num2, "é menor")


#Funçao exercicio 9
def ex9():
    print("9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.")

    num = float(input("Digite um numero: "))

    if((num % 1) == 0):
        print("Inteiro")
    else:
        print("Não é inteiro")

#Funçao exercicio 10
def ex10():
    print("10) Faça um algoritmo que verifica se um determinado valor é uma String.")

    valor = "sdf"

    if(type(valor) == str):
        print("É uma string")
    else:
        print("Não é String")

#Funçao exercicio 11
def ex11():
    print("11) Faça um algoritmo que verifica se um determinado valor é do tipo decimal.")

    valor = 10
    if(type(valor) == int):
        print("É decimal")
    else:
        print("Não é decimal")

#Funçao exercicio 12
def ex12():
    print("12) Faça um algoritmo que peça um valor numérico. Em seguida, verifique se o número é inteiro ou decimal.")

    num = float(input("Digite um numero"))

    if((num % 1) == 0):
        print("Inteiro")
    else:
        print("Decimal")

#Funçao exercicio 13
def ex13():
    print("13) Faça um algoritmo que leia três números e imprima na tela o maior deles.")

    num = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    num3 = float(input("Digite mais um número: "))

    if (num > num2 and num > num3):
        print(num, "é maior")

    if (num2 > num and num2 > num3):
        print(num2, "é maior")

    if (num3 > num and num3 > num2):
        print(num3, "é maior")

#Funçao exercicio 14
def ex14():
    print("14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.")

    num = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    num3 = float(input("Digite mais um número: "))

    if (num < num2 and num < num3):
        if (num2 < num3):
            print(num,num2,num3)
        else:
            print(num,num3,num2)

    if (num2 < num and num2 < num3):
        if(num < num3):
            print(num2,num,num3)
        else:
            print(num2,num3,num)

    if(num3 < num and num3 < num2):
        if(num < num2):
            print(num3,num,num2)
        else:
            print(num3,num2,num)

#Funçao exercicio 15
def ex15():
    print("15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.")

    valor = input("Digite um caractere")

    ct = valor.lower()

    if((ct == 'a') or (ct == 'e') or (ct == 'i') or (ct == 'o') or (ct == 'u')):
        print("Vogal")

    else:
        print("Consoante")

#Funçao exercicio 16
def ex16():
    print("16)Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.")

    valor = input("Digite o endereço ip: ")
    ip = valor.split('.')

    if(int(ip[0]) <= 127):
        print("o IP",valor,"é Classe A")
    elif(int(ip[0]) <= 191):
        print("o IP",valor,"é Classe B")
    elif(int(ip[0]) <= 223):
        print("o IP",valor,"é Classe C")
    elif(int(ip[0]) <= 239):
        print("o IP", valor,"é Classe D")
    elif(int(ip[0]) <= 254):
        print("o IP", valor,"é Classe E")
    else:
        print("Esse ip está fora do range 0 - 254")


#Funçao exercicio 17
def ex17():
    print("7) Faça um algoritmo que receba um número inteiro, que represente um determinado mês do ano, e mostre o nome do mês correspondente.")

    mes = input("Digite o número do mês: ")

    if(mes > 12):
        print("Esse mês não existe!")
    else:
        if(mes == 1):
            print("Janeiro")
        elif(mes == 2):
            print("Fevereiro")
        elif(mes == 3):
            print("Março")
        elif(mes == 4):
            print("Abril")
        elif(mes == 5):
            print("Maio")
        elif(mes == 6):
            print("Junho")
        elif(mes == 7):
            print("Julho")
        elif(mes == 8):
            print("Agosto")
        elif(mes == 9):
            print("Setembro")
        elif(mes == 10):
            print("Outubro")
        elif(mes == 11):
            print("Novembro")
        elif(mes == 12):
            print("Dezembro")

#funçao exercicio 18
def ex18():
    print("18) Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano.")

    valor = input("Digite uma data no padrão dd/mm/aa ")
    data = valor.split('/')

    if((len(data) < 3) or (len(data) > 3)):
        print("Padrão de data incorreto")

    elif((int(data[0]) < 0) or (int(data[0]) > 30)):
        print("Verifique o dia.")

    elif((int(data[1]) < 0) or (int(data[1]) > 12)):
        print("Verifique o mês")



#Funçao principal
case = input("Digite o número do exercicio: ")

if(case == '1'):
    ex1()
elif(case == '2'):
    ex2()
elif(case == '3'):
    ex3()
elif(case == '4'):
    ex4()
elif(case == '5'):
    ex5()
elif(case == '6'):
    ex6()
elif(case == '7'):
    ex7()
elif(case == '8'):
    ex8()
elif(case == '9'):
    ex9()
elif(case == '10'):
    ex10()
elif(case == '11'):
    ex11()
elif(case == '12'):
    ex12()
elif(case == '13'):
    ex13()
elif(case == '14'):
    ex14()
elif(case == '15'):
    ex15()
elif(case == '16'):
    ex16()
elif(case == '17'):
    ex17()
elif(case == '18'):
    ex18()

else:
    print("Exercicio não encontrado!")