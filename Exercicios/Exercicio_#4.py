###################
### Exercicio 1 ###
###################
def ex1():
   print("1) Escreva um algoritmo que contenha uma função de nome estudo() "
         "e que quando executada imprima na saída padrão a frase 'Estamos estudando as funções':")
   def estudo():
       print("Estamos Estudando as funções ")

   estudo()

###################
### Exercicio 2 ###
###################
def ex2():
    print("2) Escreva um código contendo uma função de nome estudo e defina que a mesma deva receber "
    "um número como argumento. Chame este argumento de x. No corpo da função imprima a seguinte "
    "frase na tela: ‘Função invocada com sucesso. O valor passado pelo argumento x é: <valor de x>’")

    num = int(input("Digite um numero: "))

    def estudo(x):
        print("Função invocada com sucesso. o Valor passado é",x)

    estudo(num)

###################
### Exercicio 3 ###
###################
def ex3():
    print("3) Escreva um algoritmo que receba dois números através da "
          "declaração de dois parâmetros cujos nomes serão: x e y. No bloco "
          "de instrução faça a soma de amb")

    x = int(input("Digite um numeros: "))
    y = int(input("Digite outro numero: "))

    def soma(num,num2):
        print(num+num2)

    soma(x,y)

###################
### Exercicio 4 ###
###################
def ex4():
    print("4) Escreva um algoritmo contendo uma função que necessite de três "
          "argumentos. Em seguida, imprima na tela os argumentos em ordem "
          "ascendente e, por fim, imprima a média aritmética:")

    num = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    num3 = int(input("Digite o terceiro numero: "))

    def media(x,y,z):
        lista = [x,y,z]
        lista.sort()              #Ordena de forma Ascendente
        print(lista)
        print((x+y+z)/len(lista)) #Média Aritimética

    media(num,num2,num3)

###################
### Exercicio 5 ###
###################
def ex5():
    print("5) Escreva uma função que contenha dois parâmetros. "
          "O primeiro deve ser obrigatório e o segundo facultativo:")

    def func(x, y=9):#Função com parêmetro obrigatório e facultativo
        print(x, y)

###################
### Exercicio 6 ###
###################
def ex6():
    print("(6) Escreva uma função que invocará outra função na qual "
          "tenha dois parâmetros definidos. Invoque a primeira função "
          "de ``func1()`` e a segunda de ``func2()``. Em seguida, "
          "invoque os parâmetros da segunda função de x e y. Some "
          "x e y e retorne o resultado. Em func1(), ao receber o "
          "resultado, retorne-o também como valor de retorno da função. "
          "Por fim, imprima na tela o valor que foi calculado por func2()"
          ", retornado para func1() e retornado a quem invocou a função "
          "inicialmente:")

    num = 1
    num2 = 2

    def func1(z):
        print(z)

    def func2(x, y):
        func1(x + y)

    func2(num, num2)

###################
### Exercicio 7 ###
###################
def ex7():
    print("7) Escreva um algoritmo capaz de receber uma quantidade"
          " variável de parâmetros. Em seguida, imprima os parâmetros"
          " recebidos na tela:")

    vlr = ''
    lista = []

    def func(*recebe):
        print(recebe)

    while(vlr != 'q'):
        vlr = input("Digite um numero: ")
        lista.append(vlr)

        func(lista)

###################
### Exercicio 8 ###
###################
def ex8():

    print("8) Escreva um algoritmo capaz de receber uma quantidade variável "
          "de parâmetros que estejam associados a uma chave. Em seguida, "
          "imprima na tela o nome da chave e o respectivo valor:")

    vlr = ''

    def dicionario(**dict):
        print(dict)

    while(vlr != 'q'):
        chave = input("Digite a chave: ")
        vlr = input("Digite o valor: ")

        dicionario(chave=vlr)
###################
### Exercicio 9 ###
###################
def ex9():

    print("Invoque a função func(), passando como argumento"
          " os valores contidos em lista, com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:")

    def func(a,b,c,d):
        print(a+b+c+d)

    lista = 1,2,3,4

    func(*lista)

####################
### Exercicio 10 ###
####################
def ex10():

    print("10) Escreva um algoritmo que encontre "
          "o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.")

    def maior(a, b, c):
        if((a > b) and (a > c)):
            return a
        elif((b > a) and (b > c)):
            return b
        else:
            return c

    num = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    num3 = int(input("Digite mais outro numero: "))

    print(maior(num, num2, num3))

####################
### Exercicio 11 ###
####################
def ex11():
    print("11) Escreva um função que some todos os números contidos numa lista."
          "Lista: (1, 2, 3, 4, 5)"
          "Soma: 15")

    lista = [1,2,3,4]

    def soma(*lista):
        print(sum(lista))

    soma(*lista)

####################
### Exercicio 12 ###
####################
def ex12():
    print("12) Escreva uma função que multiplique todos os números de uma lista."
          "Lista: (1, 2, 3, 4, 5)"
          "Multiplicação: 120")

    lista = [1, 2, 3, 4,5]


    def multiplica(temp,*lista):

        for num in lista:
            temp *= num

        print(temp)

    multiplica(*lista)

####################
### Exercicio 13 ###
####################
def ex13():
    print("13) Escreva uma função que inverta a ordem dos elementos de uma "
          "lista manualmente. Não utilize a função interna do Python que faz "
          "inverção, crie o algoritmo que faça a inversão."
          "Lista: 1234abcd "
          "Saída: dcba4321")

    lista = [1,2,3,4,'a','b','c','d']
    lista2 = list(range(len(lista)))
    num = len(lista)-1
    num2 = 0

    while(num >= 0):
        lista2[num2] = lista[num]
        num -= 1
        num2 += 1

    print(lista2)

####################
### Exercicio 14 ###
####################
def ex14():
    print("14) Escreva uma função que calcule o fatorial "
          "de um número (um inteiro não negativo). Envie o"
          "valor do número que será calcula como argumento "
          "da função.")

    numero = int(input("Digite um numero: "))

    def fatorial(num):
        aux = 1
        cont = 1

        while(cont <= num):
            aux = cont * aux
            cont += 1

        print(aux)

    fatorial(numero)

####################
### Exercicio 15 ###
####################
def ex15():
    print("15) Escreva uma função que verifique se um número está num intervalo determinado.")

    numero = int(input("Digite um numero: "))

    def intervalo( num):
        if((num >= 1) and (num <= 100)):
            print("O Numero digitado está contido entre %i e %i" %(1, 100))
        else:
            print("O Numero digitado não está dentro do intervalo!")

    intervalo(numero)

####################
### Exercicio 16 ###
####################
def ex16():
    print("16) Escreva uma função que aceite Strings e calcule a "
          "quantidade de letras em mauisculas e minúsculas que a String possui.")

    frase = input("Digite uma frase com maiuscula e minuscula: ")

    def verificamm(fra):

        maiuscula = 0
        minuscula = 0

        for letra in fra:
            if(ord(letra) > 96):
                minuscula += 1
            else:
                maiuscula += 1
        print("Sua frase Possui %i Maiusculas e %i Minusculas"%(maiuscula,minuscula))

    verificamm(frase)

####################
### Exercicio 17 ###
####################
def ex17():
    print("17) Escreva uma função que receba como argumento uma lista que poderá ter valores duplicados e retorne uma nova lista sem que haja valores iguais."
          "Lista: [1,2,3,3,3,3,4,5]"
          "Retorno: [1, 2, 3, 4, 5]")

    lista = [1,2,3,3,3,3,4,5]

    def duplicados(li):
        aux = []
        for i in li:
           if(i not in aux):
               aux.append(i)
        print(aux)

    duplicados(lista)

####################
### Exercicio 18 ###
####################
def ex18():
    print("18) Escreva uma função capaz de receber uma quantidade indeterminada "
          "de parâmetros e imprima na telas os números primos contidos nessa lista.")

    lista = range(100)

    def primos(li):
        nprimos = []

        for i in li:
            if(i > 10):
                if((i%2 != 0) and (i%3 != 0) and (i%5 != 0) and (i%7 != 0)):
                    nprimos.append(i)
            else:
                if(i == 2) or (i == 3) or (i == 5) or (i == 7):
                    nprimos.append(i)
        print(nprimos)

    primos(lista)

####################
### Exercicio 19 ###
####################
def ex19():
    print("19) Escreva uma função que imprima somente os números pares"
          "Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]"
          "Saída: [2, 4, 6, 8]")

    lista = range(30)

    def pares(li):
        aux = []

        for i in li:
            if(i%2 == 0):
                aux.append(i)
        print(aux)

    pares(lista)

####################
### Exercicio 20 ###
####################
def ex20():
    print("20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.")

    frase = input("Digite uma frase: ")

    def palindromo(fr):
        invert = fr[::-1]
        cont = 0

        for i in range(len(fr)):
            if(invert[i] == fr[i]):
                cont += 1

        if(cont == len(fr)):
            print("É um palindromo")
        else:
            print("Não é um palindromo")

    palindromo(frase)

####################
### Exercicio 21 ###
####################
def ex21():
    print("21) Escreva uma função que tenha definida"
          " uma função em seu escopo. Invoque a função"
          " aninhada, retorne algum valor, imprima esse"
          " valor na tela e finalize a aplicação.")



###################
### Função Main ###
###################
ex = int(input("Digite o numero do exercicio: "))

if(ex == 1):
    ex1()
elif(ex == 2):
    ex2()
elif(ex == 3):
    ex3()
elif(ex == 4):
    ex4()
elif(ex == 5):
    ex5()
elif(ex == 6):
    ex6()
elif(ex == 7):
    ex7()
elif(ex == 8):
    ex8()
elif(ex == 9):
    ex9()
elif(ex == 10):
    ex10()
elif(ex == 11):
    ex11()
elif(ex == 12):
    ex12()
elif(ex == 13):
    ex13()
elif(ex == 14):
    ex14()
elif(ex == 15):
    ex15()
elif (ex == 16):
    ex16()
elif (ex == 17):
    ex17()
elif (ex == 18):
    ex18()
elif (ex == 19):
    ex19()
elif (ex == 20):
    ex20()
elif (ex == 21):
    ex21()
