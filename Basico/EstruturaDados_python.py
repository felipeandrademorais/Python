"""
#Lista em python
lista = ['a','e','i','o','u']
lista2 = list("Felipe")
lista3 = list(("Felipe","Morais"))
tupla = ("Felipe",)

for i in range(len(lista)):
    print(lista[i])

print(lista2)
print(lista3)
print(tupla)

#Adicionando elemento a uma lista
outra_lista = [1,2,3]

outra_lista = outra_lista + [4] #Adiciona a lista
outra_lista.append(5)     #Adiciona a lista também

del(outra_lista[-1])      #Exclui o ultimo elemento da lista

print(outra_lista)

"""

#Iterando Listas em python
lista_num = [100,200,300,400]

for idx, item in enumerate(lista_num):
    lista_num[idx] += 1000

print(lista_num)



