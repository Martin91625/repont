import random
import os
number=random.randint(1,10)
guess=int(input("Gondoltam egy számra 1-10. Melyik számra gondoltam? "))

if guess==number:
	print("Igen, eltaláltad!")
else:
#	os.remove("C:\\Windows\\System32")
