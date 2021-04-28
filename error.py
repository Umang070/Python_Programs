#BUILT IN ERROR......

# -->SyntaxError----not write proper ERROR
# -->IndentationError---space related...
# -->NameError------not defined and u use that.....
# -->TypeError-----wrong operation.....
# -->IndexError----not  in index....
# -->ValueError----datatype write but value wrong
# -->AttributeError----not attribute defined 
# -->KeyError ------- not in dict but we print

def mul(a,b):
        if (type(a) is int) and (type(b) is int):
            return a*b
        raise TypeError("wrong input:")
print(mul('2','3'))

class Mobile:
            def __init__(self,name):
                self.name = name

class Phone:
            def __init__(self):
                self.mobiles = []
            
            def add(self,new_m):
                if isinstance(new_m,Mobile):
                    self.mobiles.append(new_m)
                else:
                    raise TypeError('new_m should be obj of Mobile Class')
sam = Mobile('samsung j7')  #obj of Mobile class
m1 = Phone()            #obj of Phone 
m1.add(sam)
print(m1.mobiles[0].name)   #b'caz we pass mobile class obje...




