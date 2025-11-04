lista=[]
for i in range(5):
	szam=int(input("Kérek egy számot "))
	lista.append(szam)

for i in range(len(lista)):
	if i!=len(lista)-1:
		print(lista[i],end=", ")
	else:
		print(lista[i])
