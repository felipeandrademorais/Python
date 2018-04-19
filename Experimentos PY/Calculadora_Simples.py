def soma (num1,num2):
    print(num1+num2)

def subtracao(num1,num2):
    print(num1-num2)

def divisao(num1,num2):
    print(num1/num2)

def multiplicacao(num1,num2):
    print(num1*num2)

while(True):
    numero1 = int(input("Digite um numero"))
    numero2 = int(input("Digite outro numero"))

    operacao = input("Qual operação deseja fazer? \n+ Soma\n- Subtração\n/ Divisão\n* Multiplicação")

    if(operacao == '+'):
        soma(numero1,numero2)
    elif(operacao == '-'):
        subtracao(numero1,numero2)
    elif(operacao == '/'):
        divisao(numero1,numero2)
    elif(operacao == '*'):
        multiplicacao(numero1,numero2)



