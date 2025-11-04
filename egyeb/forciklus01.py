'''
100 elemű lista random számokból (100-300)
'''
lista=[]
import random
for i in range(100):
	szam=random.randint(100,300)
	lista.append(szam)

for i in range(len(lista)):
	if i!=99:
		print(lista[i],end=", ")
	else:
		print(lista[i])
