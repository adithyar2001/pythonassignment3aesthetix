class parent:
    def function1(self):
        print("parent class")
        
class child(parent):
    def function2(self):
        print("child class")
obj1 = child()
obj1.function1()
obj1.function2()