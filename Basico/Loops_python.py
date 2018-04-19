"""
#Lista de 0 a 100 com intervalos de 10
print(list(range(0,100,10)))

#range junto com a instrução for
for i in range(10):
    if(i == 8):
        break
    else:
        print(i)
"""
#Instrução Continue
for i in range(10):
    if(i%2==0):
        continue
        print(i)
