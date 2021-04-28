#encapsulation....abstraction(hide complxity form user)
# some specilal naming convention(_name means it is treated as a private) ......name mangling 
#------__name__ ---dunder [magic methods]


class Mobile:
            def __init__(self,brand,model,price):
                self.brand_name = brand
                self.model_name = model
                self._price = max(price,0)
            
            @property
            def complete_info(self):
              return f"{self.brand_name} {self.model_name} and price is : {self._price}"  

            @property       #getter.......
            def price(self):
                return self._price              
            
            @price.setter
            def price(self,new_price):
                self._price = max(new_price,0)

            def call_phone(self,ph_no):
                print(f"calling {ph_no}.....")
            
            def phone_name(self):
                return f"{self.brand_name}{self.model_name}"

m1 = Mobile('samsung','j7',100000)
# print(m1._Mobile__price)
#print(m1.__dict__)
m1._price= -45      #not solve pro b'caz it's print (-) for this use getter and setter methodss........
print(m1.price)        
print(m1.complete_info)
