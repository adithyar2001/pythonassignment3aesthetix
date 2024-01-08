class parent:
	def function1(self):
		print("parent class")


class child1(parent):
	def function2(self):
		print("child1 class")


class child2(parent):
	def function3(self):
		print("child2 class")


class child3(child2,parent):
	def function4(self):
		print("child3 class")

obj = child3()
obj.function1()
obj.function3()
obj.function4()
