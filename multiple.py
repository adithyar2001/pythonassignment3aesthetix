class sum:
    def add(self,a,b):
        return print("sum:",a+b)

class sub:
    def minus(self,a,b):
        return print("difference:",a-b)
    
class product:
    def mul(self,a,b):
        return print("product:",a*b)
    
class modulus:
    def mod(self,a,b):
        return print("modulus:",a%b)

class division(sum,sub,product,modulus):
    def div(self,a,b):
        return print("division:",a/b)
    
newcalc = division()
newcalc.add(10,2)
newcalc.minus(10,2)
newcalc.mul(10,2)
newcalc.mod(10,2)
newcalc.div(10,2)
