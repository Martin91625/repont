import random
import math
lista=[]
hlista=[]
nhlista=[]

for i in range(100):
	lista.append(random.randint(-50,50))
for number in lista:
	for i in range(10):
		if number>0 and math.pow(2,i+1)==number:
			hlista.append(number)
for number in lista:
	if number not in hlista:
		nhlista.append(number)

print(lista)
print()
print(hlista)
print()s
print(nhlista)
