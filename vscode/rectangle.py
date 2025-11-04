import dataInput
areaMenuItems="[1] Terület:[2] Kerület:[3] Mégse"
def setAreaMenuItems():
    menuSp=areaMenuItems.split(":")
    for item in menuSp:
        print(item)
def choose(number01,number02):
    while(True):
        setAreaMenuItems()
        choose=dataInput.getInteger("Válassz: ")
        match(choose):
            case 1:
                result=calcArea(number01,number02)
                print(result, "cm2")
                break
            case 2:
                result=calcPher(number01,number02)
                print(result, "cm") 
            case 3:
                break
            case __:
                print("Nincs ilyen lehetőség")
                
def calcArea(number01,number02):
    result=number01*number02
    return result

def calcPher(number01,number02):
    result=2*number01+2*number02
    return result
