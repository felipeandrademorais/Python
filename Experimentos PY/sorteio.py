import random

def sorteio():
	#Gera numero aleatorio e inclui na lista
	num = random.randrange(quantidade)

	while num in lista:
		num = random.randrange(quantidade)

	lista.append(num)
	print(num)

quantidade = int(input("Digite o total de participantes: "))
lista = []
x = ''

while(x!='q'):
	sorteio()
	x = input("Deseja continuar \n 's' para sim 'q' para sair: ")




