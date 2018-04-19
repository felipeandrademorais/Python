#Declarando um dicionário
d1 = {}
print(type(d1))

#Inicializando um dicionário
d1['aaa'] = 1000
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)

#Inicializando um dicionário 2
d2 = {1.1:"teste1",2.2:"teste2",3:"teste3"}
print(d2)

#Utilidade de um Dicionário
tel = {30301122:"Pericles",33547877:"Menelau",33381245:"Atreu",36458899:"Tieste"}
print(tel)
print(len(tel))

#Remover elemento Biblioteca
del(tel[36458899])
print(tel)

#Retorna a lista de chaves do dicionario
print(tel.keys())

#Retorna os valores associados as chaves do dicionario
print(tel.values())

#Retornao valor associado a uma chave
print(tel.get(30301122))

#Retorna um elemento e já remove do dicionario
print(tel.popitem())
print(tel)

#Verifica se um valor está condido dentro do dicionario
print(30301122 in tel)

#mesca dicionario com outro
tel2 = {99999999:"teste1",55551111:"teste2"}
tel.update(tel2)

print(tel)