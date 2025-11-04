import dataInput
import math
areaMenuItems="[1] Terület:[2] Kerület:[3] Mégse"
def setAreaMenuItems():
    menuSp=areaMenuItems.split(":")
    for item in menuSp:
        print(item)
def choose(number01,number02,number03):
    while(True):
        setAreaMenuItems()
        choose=dataInput.getInteger("Válassz: ")
        match(choose):
            case 1:
                result=calcArea(number01,number02,number03)
                print(result, "cm2")
                break
            case 2:
                result=calcPher(number01,number02,number03)
                print(result, "cm")
                break
            case 3:
                break
            case __:
                print("Nincs ilyen lehetőség")

def calcPher(number01,number02,number03):
    result=number01+number02+number03
    return result

def calcArea(number01,number02,number03):
    s=calcPher(number01,number02,number03)/2
    result=math.sqrt(s*(s-number01)*(s-number02)*(s-number03))
    return result
        