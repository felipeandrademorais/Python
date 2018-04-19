import random
import numpy as np

def derivada(n):
	return n * (1 - n)

x = 0.85
y = 0.50
w = random.random()

#época

for i in range(100):
	a = np.tanh(x * w)
	e = y - a
	w += x * derivada(e)

	print(a)