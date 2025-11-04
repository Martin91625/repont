lista=[]
szamlalo=0
import random
for i in range(1000):
	szam=random.randint(-100,100)
	lista.append(szam)

for i in range(len(lista)):
	if lista[i]<0:
		szamlalo+=1
	
	if i!=len(lista)-1:
		print(lista[i],end=", ")
	else:
		print(lista[i])

print ("Ennyi negatív van benne",szamlalo,"db")
