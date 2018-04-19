#Função com Parâmetros Default
def login(usuario="root", senha="123"):
    print("Usuario: ", usuario)
    print("Senha: ", senha)

login("Felipe","FeLi2705")#A passagem de argumentos é opcional


#Função com argumentos posicionais e nomeados
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
        .format(nome, sobrenome, idade, sexo))

dados_pessoais("Felipe","Andrade",24, True)
dados_pessoais(nome="Claudio", sobrenome="Carvalho", idade=30, sexo=True)

#Funções Variáticas
def lista_de_argumentos(*lista):
    print(lista)

def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("Um","Dois","Tres","Quatro")

lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativos(um=1, dois=2, tres=3, quatro=4)

#Desempacotamento de listas
def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "Felipe", "Andrade", 24
lista = ["Felipe","Andrade",24]
dicionario = {"nome":"Felipe","sobrenome":"Andrade",
              "idade":24}

pessoa(*tupla)
pessoa(*lista)
pessoa(**dicionario)

#Exemplo Desempacotamento
lista = [11,10,12]
tupla = 11,10,12

def func(a,b,c):
    print(a)
    print(b)
    print(c)

lista.sort()#Ordena uma lista

func(*lista)

l = [*tupla]#joga uma tupla dentro de uma lista
l.sort()
func(*l)

