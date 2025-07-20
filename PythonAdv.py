#self keyword is very important to call variable in method
#there are two types of variable class variables and instance variables

def addnum(a,b,name):
    print("hello "+name+" here is your output: ")
    return a+b

c=addnum(10,20,"Brad")
print(c)


class Calculator:
    d=100 #this is class variable

    def getData(self):
        print("getting data")
        print(self.a+self.b)

    #constructor name is always __init__
    def __init__(self,a ,b):
        print("i am constructor")
        self.a=a   #these are instance or object specific variable
        self.b=b

obj1=Calculator(3,4)
obj1.getData()
obj2=Calculator(9,9)
obj2.getData()
print(Calculator.d)