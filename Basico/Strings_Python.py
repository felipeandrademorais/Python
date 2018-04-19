# coding: utf-8
s1 = 'String com aspas simples'
s2 = "String com aspas duplas"
s3 = '''String com 3 aspas simples mais utilizado para escrever grandes textos este inclui o /n'''
s4 = """String com 3 aspas duplas este nao inclui o /n """
s = "Para o Python, toda String é uma lista imutável."

#Fatia a String
print(s[0::2])

#Retorna o código ASC da letra
ord("d")

#Retorna a letra do numero da tabela ASC
chr(100)

#Substitui parte de uma string
s.replace("Para"," ")

#Iterar string
for c in s:
    print(c)

#Iterar String 2
indice = 0

while indice < len(s):
    print(indice, s[indice])
    indice+=1

#Iterar String 3
for k,v in enumerate('Iterando Strings'):
    print(k, v)
