class parent:
    def function1(self):
        print("parent class")
        
class child1(parent):
    def function2(self):
        print("first child class")

class child2(parent):
    def function3(self):
        print(" second child class")
obj1 = child1()
obj2 = child2()
obj1.function1()
obj1.function2()
obj2.function3()
obj2.function1()
obj1.function2()
obj2.function3()