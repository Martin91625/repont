import math

#A program tároló, ellenőrző és számoló egysége

class Triangle:
    def __init__(self):
        pass
        
    def getTriSides(self):
        a = self.getFloat("\"A\" oldal: ")
        b = self.getFloat("\"B\" oldal: ")
        c = self.getFloat("\"C\" oldal: ")
        success = self.checkTriangle(a, b, c)
        while(not success):

            print("Hibás adat(ok). Az adatoknak többnek kell lennie mint 0 és a háromszögnek szerkeszthetőnek kell lennie \n ")
            a = self.getFloat("\"A\" oldal: ")
            b = self.getFloat("\"B\" oldal: ")
            c = self.getFloat("\"C\" oldal: ")
            success = self.checkTriangle(a, b, c)

        Triangle.a = a
        Triangle.b = b
        Triangle.c = c

    def checkTriangle(self, a, b, c):
        if (a <= 0 or b <= 0 or c <= 0):
            return False
        elif (a > b + c or b > a + c or c > a + b):
            return False
        else:
            return True

    def calcPherTriangle(self, a, b, c):
        return a + b + c
    
    def calcAreaTriangle(self, a, b, c):
        s = self.calcPherTriangle( a, b, c ) * 0.5
        area = math.sqrt(s *  (s - a) * (s - b) * (s - c))
        return area

    def chooseMethodTriangle(self):
        while(True):
            
            print()
            self.setAreaMenuItems()
            choice = self.getInt("Válassz: ")

            match(choice):
                case 1:
                    print("Kerület kiszámítása. . .")
                    print("A háromszög kerülete:", self.calcPherTriangle(Triangle.a, Triangle.b, Triangle.c),"cm\n")
                    break
                case 2:
                    print("Terület kiszámítása. . .")
                    print("A háromszög területe:", self.calcAreaTriangle(Triangle.a, Triangle.b, Triangle.c),"cm2\n")
                    break
                case 3:
                    print("Visszalépés. . .")
                    break
                case __:
                    print("Hibás választás. Válassz újra! (1 - 3) ")

class Circle:
    def __init__(self):
        pass      

    def getCircRad(self):
        r = self.getFloat("A kör sugara: ")
        success = self.checkCircle(r)
        while (not success):

            print("Hibás adat. Az adatoknak többnek kell lennie mint 0 \n ")
            r = self.getFloat("A kör sugara: ")
            success = self.checkCircle(r)

        Circle.r = r

    def checkCircle(self, r):
        if (r <= 0):
            return False
        else:
            return True
    
    def calcPherCircle(self, r):
        return 2 * r * math.pi
        
    def calcAreaCircle(self, r):
        return math.pow(r, 2) * math.pi
    
    def chooseMethodCircle(self):
        while (True):

            print()
            self.setAreaMenuItems()
            choice = self.getInt("Válassz: ")

            match(choice):
                case 1:
                    print("Kerület kiszámítása. . .")
                    print("A kör kerülete:", self.calcPherCircle(Circle.r),"cm\n")
                    break
                case 2:
                    print("Terület kiszámítása. . .")
                    print("A kör területe:", self.calcAreaCircle(Circle.r),"cm2\n")
                    break
                case 3:
                    print("Visszalépés. . .")
                    break
                case __:
                    print("Hibás választás. Válassz újra! (1 - 3) ")

class Rectangle:
    def __init__(self):
        pass

    def getRectSides(self):
        a = self.getFloat("\"A\" oldal: ")
        b = self.getFloat("\"B\" oldal: ")
        success = self.checkRectangle(a, b)
        while (not success):

            print("Hibás adat(ok). Az adatoknak többnek kell lennie mint 0 \n ")
            a = self.getFloat("\"A\" oldal: ")
            b = self.getFloat("\"B\" oldal: ")
            success = self.checkRectangle(a, b)
            
        Rectangle.a = a
        Rectangle.b = b

    def checkRectangle(self, a, b):
        if (a <= 0 or b <= 0):
            return False
        else:
            return True

    def calcPherRectangle(self, a, b):
        return 2 * (a + b)
    
    def calcAreaRectangle(self, a, b):
        return a * b
        
    def chooseMethodRectangle(self):
        while (True):
            
            print()
            self.setAreaMenuItems()
            choice = self.getInt("Válassz: ")

            match(choice):
                case 1:
                    print("Kerület kiszámítása. . .")
                    print("A téglalap kerülete:", self.calcPherRectangle(Rectangle.a, Rectangle.b),"cm\n")
                    break
                case 2:
                    print("Terület kiszámítása. . .")
                    print("A téglalap területe:", self.calcAreaRectangle(Rectangle.a, Rectangle.b),"cm2\n")
                    break
                case 3:
                    print("Visszalépés. . .")
                    break
                case __:
                    print("Hibás választás. Válassz újra! (1 - 3) ")        