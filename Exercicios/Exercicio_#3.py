# Ex1
def ex1():
    print("1) Faça um algoritmo que imprima os números no intervalo entre 1 e 100:")

    for i in range(1,101):
        print(i)
# Ex2
def ex2():
    print("2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido"
          " para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja "
          "que seja impresso:")

    num1 = int(input("Digite o numero inicial do intervalo : "))
    num2 = int(input("Digite o numero final do intervalo: "))

    for i in range(num1,num2):
        print(i)

# Ex3
def ex3():
    print("3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:")

    for i in range(10,0,-1):
        print(i)

# Ex4
def ex4():
    print("4) Faça um algoritmo que imprima os números pares entre 0 e 100:")

    for i in range(101):
        if(i%2==0):
            print(i)
# Ex5
def ex5():
    print("5) Faça um algoritmo que some a quantidade de números pares encontrados no intervalo entre 0 e 100:")

    soma = 0
    for i in range(0,101):
        if(i%2==0):
            soma += i
    print(soma)

# Ex6
def ex6():
    print("6) Faça um algoritmo que imprima os números primos entre 0 e 100: ")

    for i in range(0,101):
        if(i==1 or (i!=2 and i%2==0)):
            pass
        elif(i!=3 and i%3==0):
            pass
        elif(i!=5 and i%5==0):
            pass
        elif(i!=7 and i%7==0):
            pass
        else:
            print(i)

# Ex7
def ex7():
    print("7) Faça um algoritmo que calcule os número primos num "
          "intervalo pré-determinado pelo usuário:")

    num = int(input("Digite o valor inicial do range: "))
    num2 = int(input("Digite o valor final do range: "))

    for i in range(num,num2):
        if(i==1 or (i!=2 and i%2==0)):
            pass
        elif(i!=3 and i%3==0):
            pass
        elif(i!=5 and i%5==0):
            pass
        elif(i!=7 and i%7==0):
            pass
        else:
            print(i)

def ex8():
    print("8) Faça um algoritmo que imprima os valores no "
          "intervalo definido pelo usuário e permita que o "
          "mesmo possa definir 3 números que deverão ser ignorados, "
          "ou seja, que não serão impressos na tela:")

    num = int(input("Digite um numero para não ser exibido de 0 a 100: "))
    num2 = int(input("Digite outro numero para não ser exibido de 0 a 100: "))
    num3 = int(input("Digite outo numero para não ser exibido de 0 a 100: "))

    for i in range(101):
        if((i!=num) and (i!=num2) and (i!=num3)):
            print(i)

def ex9():
    print("9) Faça um algoritmo que imprima a frase 'estou em looping' e,"
          " em seguida, solicite ao usuário digitar uma letra. Caso a "
          "letra seja o 'q' finalize a aplicação. Do contrário, imprima "
          "novamente a mesma frase até que o caractere 'q' seja enviado:")

    while(True):
        num=input("Estou em looping")
        if((num == 'q')or(num == 'Q')):
            break

#Funcao Menu inicial
case = int(input("Digite o numero do Exercicio: "))

if(case == 1):
    ex1()
if(case == 2):
    ex2()
if(case == 3):
    ex3()
if(case == 4):
    ex4()
if(case == 5):
    ex5()
if(case == 6):
    ex6()
if(case == 7):
    ex7()
if(case == 8):
    ex8()
if(case == 9):
    ex9()

