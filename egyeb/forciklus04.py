lista=[]
import random
for i in range(1000):
	szam=random.randint(-100,100)
	lista.append(szam)

for i in range(len(lista)):
	if i!=len(lista)-1:
		print(lista[i],end=", ")
	else:
		print(lista[i])
ossz=sum(lista)
print(ossz)
