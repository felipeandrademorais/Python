lista = ['Felipe', 'Renata', 'Maria', 'Jose', 'João', 'Fulano']

#inverte a ordenação da lista
lista.reverse()

#Ordena a lista de forma ascendente
lista.sort()

#Ordena a lista de forma descendente
lista.sort(reverse=True)

#Conta quantas veses o elemento se repete
lista.count('Felipe')

#Retorna a posição do elemento
lista.index('Renata')

#Verifica se o valor está contido na lista, retorna True or False
'Maria' in lista
'Jose' not in lista

#Verifica se varios valores estão contidos em uma lista
'Maria' and 'Jose' in lista
'Maria' or 'Jose' in lista


