#......MULTIPLE INHERITANCE...........

class A:
        def class_a(self):
            return " i \'m method of class A"
        def hello(self):
            return "hello from class A:"

class B:
        def class_b(self):
            return " i /'m method of class B"
        def hello(self):
            return "hello from class B:"

class C(B,A):               #if we open MRO then .....First C...B.....A
            pass

c1=C()
print(c1.class_a())
print(c1.hello())
print(C.__mro__)      #for MRO.......... (C.mro())


#............DUNDER METHODS.............

class Mobile:
            def __init__(self,brand,model,price,number):
                self.brand_name = brand
                self.model_name = model
                self._price = max(price,0)
                self.no = number
            
            def complete_info(self):
              return f"{self.brand_name} {self.model_name} and price is : {self._price}"  

            def __str__(self):      #nyc formatting string.........
              return f" {self.model_name} and price is : {self._price}"  

            def __repr__(self):     #for devlopers.......debugging
              return f'Mobile (\'{self.brand_name}\' ,  {self._price})' 
            
            def __len__(self):
              return len(self.brand_name)  #len(self.m1()) ??

            def __add__(self,ref):      #own method
                return (self._price + ref._price),(self.no + ref.no)

m1 = Mobile("samsung","j7",10000,10)
m2 = Mobile("onplus","6t",36000,20)
print(len(m1))      #why do not print this............
   #print(m1.__repr__())  or...........print(str(m1))
print(m1)#by __str__mehod..we override that.......
print( m1 + m2)   #Mobile.add(m1,m2)....