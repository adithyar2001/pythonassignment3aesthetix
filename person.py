class person:
    def __init__(self,name,age,address):
        self.names = name
        self.ages=age
        self.addresses = address
        
    def func2(self,newname,newage,newaddress):
        self.names = newname
        self.ages=newage
        self.addresses = newaddress
        
    def prints(self):
        print("name",self.names)
        print("age",self.ages)
        print("address",self.addresses)
p1 = person(name="henry",age=10,address="delhi")
p1.prints()
print("new information")
p1.func2(newname="harry",newage=13,newaddress="agra")
p1.prints()