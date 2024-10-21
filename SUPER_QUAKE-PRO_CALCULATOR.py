import math
# QUAKE-PRO calculator by D.

class OneFunc:
    def take(self):
        try:
            a = float(input("Введите "+self.aS+" - "))
            self.a = a
        except:
            print("это не число")
            self.a = None
    def __init__(self):
        self.aS = ""

class TwoFunc:
    def take(self):
        try:
            a = float(input("Введите "+self.aS+" - "))
            print("")
            b = float(input("Введите "+self.bS+" - "))
            self.a = a
            self.b = b
        except:
            print("это не число")
            self.a = None
            self.b = None
    def __init__(self):
        self.aS = ""
        self.bS = ""

class Add(TwoFunc):
    def __init__(self):
        self.aS = "первое слогаемое"
        self.bS = "Второе слогаемое"
    def ex(self):
        return self.a + self.b

class Sub(TwoFunc):
    def __init__(self):
        self.aS = "уменьшаемое"
        self.bS = "вычитаемое"
    def ex(self):
        return self.a - self.b

class Mul(TwoFunc):
    def __init__(self):
        self.aS = "первый множитель"
        self.bS = "второй множитель"
    def ex(self):
        return self.a * self.b

class Div(TwoFunc):
    def __init__(self):
        self.aS = "делимое"
        self.bS = "делитель"
    def ex(self):
        return self.a / self.b

class Pow(TwoFunc):
    def __init__(self):
        self.aS = "число"
        self.bS = "степень"
    def ex(self):
        return self.a ** self.b

class Root(OneFunc):
    def __init__(self):
        self.aS = "число"
    def ex(self):
        return self.a ** (0.5)

class Sin(OneFunc):
    def __init__(self):
        self.aS = "угол"
    def ex(self):
        return round(math.sin(self.a*3.1415926535/ 180.0),5)

class Cos(OneFunc):
    def __init__(self):
        self.aS = "угол"
    def ex(self):
        return round(math.cos(self.a*3.1415926535/ 180.0),5)

class Tan(OneFunc):
    def __init__(self):
        self.aS = "угол"
    def ex(self):
        return round(math.tan(self.a*3.1415926535/ 180.0),5)

class Cotan(OneFunc):
    def __init__(self):
        self.aS = "угол"
    def ex(self):
        return round(1.0/math.tan(self.a*3.1415926535/ 180.0),5)

class Log(TwoFunc):
    def __init__(self):
        self.aS = "основание"
        self.bS = "число"
    def ex(self):
        return math.log(self.a,self.b)
op = (
"сложение", "вычитание", "умножение", "деление",
"степень", "корень",
"синус", "косинус", "тангенс", "котангенс",
"логарифм")
func = (Add(),Sub(),Mul(),Div(),Pow(),Root(),Sin(),Cos(),Tan(),Cotan(),Log())
def comm(n):
    r = None
    try:
        n = int(n) -1
        f = func[n]
        f.take()
        if f.a != None:
            r = f.ex()
            return r
        else:
            return None
    except:
        print("нету такого варианта.")
    return None

def choice(l):
    print("\n"+": "*20)
    for i in op:
        print(f"{op.index(i)+1}. - {i}",end = "")
        if (op.index(i) + 1)%2 == 0:
            print(" "*(12 - len(i)-op.index(i)//9)+".")
        else:
            print(" "*(15 - len(i)-op.index(i)//9)+".",end=" ")
    print("\n"+" ."*20)
    print("\n\nнажмите [Q], чтобы выйти")
    i = input("\n\nВаш выбор:")
    return i
print("""
#-- # # ##\ ### ##\ 
/_# # # #_# #-- #_#
__/ ##/ #   ### # \ 

##\ # # ##\ # / ###     ##\ ##\ ##\ 
# # # # #-# ##  #-- --- #_# #_# # #
\#\ ##/ # # # \ ###     #   # \ ###

### ##\ #   ### # # #   ##\ ### ##\ ##\ 
#   #-# #   #   # # #   #-#  #  # # #_#
### # # ### ### ##/ ### # #  #  ### # \ 

- super QUAKE-PRO калькулятор.
""")
while True:
    f = choice(op)
    if f == "q":
        break
    print("-"*10)
    f = comm(f)
    if f != None:
        print("="*10)
        print("ответ:",f)
        print("="*10)
print("Завершение программы...")