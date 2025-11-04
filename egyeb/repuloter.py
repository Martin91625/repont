'''
File: repuloter.py
Author: El Miri Martin
Copyright: 2025, El Miri Martin
Date: 2025.09.25
Web: http://martinweboldala.hu (nem létezik még, de majd fog)
Licenc: nincs de majd lesz 
'''
velocity=-1
angle=-1
cloud=-1
print("Készítő: El Miri Martin")
print("A program bekéri az időjárási viszonyokat, és kiszámolja, hogy megengedett-e a felszállás az 1-es kifutón")
print()
while velocity<0 or velocity>500:
	velocity=int(input("Kérem a szélsebességet: (0-500 km/h) "))
	if velocity<0 or velocity>500:
		print("Hibás adat, kérem adja meg újra")
		
while angle<0 or angle>180:
	angle=int(input("Kérem a szélirányt az 1-es kifutóhoz képest (0°-180°) "))
	if angle<0 or angle>180:
		print("Hibás adat, kérem adja meg újra")
		
while cloud<0 or cloud>100:
	cloud=int(input("Kérem a felhők arányát az égen (1-100) "))
	if cloud<0 or cloud>500:
		print("Hibás adat, kérem adja meg újra")

permission=True
recommended=True
if velocity>100:
	permission=False
if velocity>50 and angle>54:
	recommended=False
if cloud>45:
	permission=False

if permission==False:
	print("Tiltott felszállás")
elif recommended==False:
	print("Nem ajánlott a felszállás")
else:
	print("A felszállás megengedett")
