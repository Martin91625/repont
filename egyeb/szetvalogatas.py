import random
lista=[]
nlista=[]
plista=[]
for i in range(500):
	lista.append(random.randint(-100,100))
'''
for i in range(len(lista)):
	if lista[i]<0:
		nlista.append(lista[i])
	else:
		plista.append(lista[i])
'''
for number in lista:
	if number<0:
		nlista.append(number)
	else:
		plista.append(number)
print(lista)
print(plista)
print(nlista)
	
