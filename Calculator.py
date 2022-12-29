class Calculator:
    def __init__(self):
        self.x=int(input("Enter First Number = "))
        self.y=int(input("Enter First Number = "))
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
    def sub(self):
        return self.x-self.y
    def div(self):
        return self.x/self.y
    def percentage(self):
        return (self.x/self.y)*100

        
while True:
    C =Calculator()
    print(''' What You Want to DO?
              1.Sum 
              2.Substract 
              3.Divide 
              4.percentage 
              5.multiply ''')
    ch=int(input("Enter The Above Number of the list ? "))
    if ch==1:
        print(f"The Sum Of {C.x} and {C.y} = {C.add()}")
    elif ch==2:
        print(f"The Substract Of {C.x} and {C.y} = {C.sub()}")
    elif ch==3:
        print(f"The Divide Of {C.x} and {C.y} = {C.div()}")
    elif ch==4:
        print(f"The Percentage Of {C.x} and {C.y} = {C.percentage()}")
    elif ch==5:
        print(f"The Multiply Of {C.x} and {C.y} = {C.mul()}")
    else:
        print('wrong Input')