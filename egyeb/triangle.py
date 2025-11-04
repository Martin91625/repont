import math
def getNumber(text):
	number=float(input(text))
	return number

def checker(sideList):
	if(sideList[0]+sideList[1]>sideList[2] and 
	sideList[0]+sideList[2]>sideList[1] and 
	sideList[1]+sideList[2]>sideList[0]):
		return True
	else:
		return False

def pherCalculate(sideList):
	result=0
	for side in sideList:
		result+=side
	return result
		
def areaCalculate(sideList):
	result=0
	s=pherCalculate(sideList)/2
	result=math.sqrt(s*(s-sideList[0])*(s-sideList[1])*(s-sideList[2]))
	return result

'''
def checkChoice(choose):
	choose=getNumber("kerület(1) vagy terület(2) ")
	match(choose):
		case 1:
			pherCalculate()
		case 2:
			areaCalculate()
'''	
def controller():
	sideList=[]
	sideList.append(getNumber("A oldal: "))
	sideList.append(getNumber("B oldal: "))
	sideList.append(getNumber("C oldal: "))
	success=checker(sideList)
	print(success)
	if(success):
		pher=pherCalculate(sideList)
		area=areaCalculate(sideList)
		
controller()
