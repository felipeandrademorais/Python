"""
### 1) Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.

nome = input("Seu Nome: ")
print(nome)

### 2) Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão: "O seu nome é: [nome do usuário]".

nome = input()
print("Seu nome é:", nome)

### 3) Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: "O seu nome é <nome> e a sua idade é <idade>".

nome = input("Seu nome ")
idade = input("Sua idade ")

print("O seu nome ",nome,"sua idade ",idade)

### 4) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável e por fim, envie esse número para a saída padrão.

num = input("Digite um numero ")
print("Numero ",num)

### 5) Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem: "O número digitado foi: ".

num = input("Digite um numero ")
print("o numero digitado foi ",num)

### 6) Faça um algoritmo que solicite ao usuário informar 3 números. Em seguida, some-os e envie para a saída padrão a seguinte frase: "A soma total é: "

num1 = int(input("Digite primeiro numero "))
num2 = int(input("Digite segundo numero "))
num3 = int(input("Digite terceiro numero "))

print("A soma total é: ", num1+num2+num3)

### 7) Faça um algoritmo que solicite ao usuário informar 2 números.
#Em seguida, some os valores e envie para a saída padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".

num1 = int(input("Digite primeiro numero "))
num2 = int(input("Digite segundo numero "))

print("A soma entre %i e %i é igual a:" %(num1,num2), (num1 + num2))

### 8) Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a saída padrão a média:

nt1 = float(input("Primeira nota "))
nt2 = float(input("Segunda nota "))
nt3 = float(input("Terceira nota "))
nt4 = float(input("Quarta nota "))

print("### Média das notas: ", ((nt1+nt2+nt3+nt4)/4), "###")


### 9) Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta essa medida para centímetros e envie para a saída padrão:

mt = float(input("Digite valor em metros "))

cm = mt * 100

print("Convertido em Centímetros:", cm)

### 10) Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:

num = int(input("Digite um número "))

print("Cubo:",(num**3)," Quadrado:",(num**2))

### 11) Faça um algoritmo que solicite ao usuário digitar 2 números.
### Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):

num = float(input("Digite um numero "))
num2 = float(input("Digite outro numero "))

print("Divisão Decimal:",(num/num2), "Divisão Inteiro:",(num//num2) )

### 12) Faça um algoritmo que solicite a largura e a altura de um quadrado. Em seguida,
###  imprima para o usuário quantos metros quadrados possui a área total do quadrado.

lag = float(input("Digite a Largura "))
alt = float(input("Digite a altura "))

print("Área do quadrado:",(lag*alt))

### 13) Faça um algoritmo que solicite ao usuário informar uma quantidade de dias,
###  horas, minutos e segundos. Em seguida, converta tudo para segundos:

dias = int(input("Digite dias "))
horas = int(input("Digite horas "))
minutos = int(input("Digite minutos "))
segundos = int(input("Digite segundos "))

print("Convertendo sem segundos", ((dias * 86400) + (horas * 3600) + (minutos * 60) + segundos))

### 14) Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida,
### aplique 10% de desconto e imprima na tela tanto o valor total como também o valor com o desconto aplicado.

valor = float(input("Digite o valor "))

print("valor Total %.2f e Valor com desconto" %valor, (valor - (valor * 0.1)))

"""

