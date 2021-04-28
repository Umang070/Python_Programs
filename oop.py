class Car:
            Percentage_dis = 10
            def __init__(self,car_name,price):
                #instance variables
                #print("init method")
                self.car_name = car_name
                self.price = price
                
    
            def car_model_with_price(self):
                return (f"{self.car_name} and  {self.price}")
    
            def is_higher(self):
                return self.price > 1000000
    
            def discount(self):
                dic_price = (self.price * self.Percentage_dis)/100
                final_price = self.price -dic_price
                return f"final price is {final_price}"





c1 = Car("farrari",15000000)
c2 = Car("BMW",10000000)

# print(c1.car_name)
# print(c1.price)
print(c1.car_model_with_price())        #  same as ...............Car.car_model_with_price(c1)
print(c1.is_higher())
print(c1.discount())                    # for this dis is 10
c2.Percentage_dis = 0   #if change particular dis then go to function and change by self......
print(c2.__dict__)
print(c2.discount())



# -----------second class-----------

# class Circle:
#                 pi = 3.14       #CLASS VARIABLE
#                 def __init__(self,rad):
#                     self.radius = rad
                    
#                 def area_c(self):
#                     area = ( Circle.pi * (self.radius ** 2) )
#                     return f"area of circle is : {area}"
#                 def circumfarance(self):
#                     cir = 2 * Circle.pi * self.radius
#                     return f"circumfarance of circle is : {cir}"

# c1 = Circle(4)
# print(c1.area_c())
# print(c1.circumfarance())