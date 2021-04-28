#multilevel inheritance.....method resolution order
#method overriding..........isinstance(object is belong to particular_class or not ) , issubclass()
class Mobile:
            def __init__(self,brand,model,price):
                self.brand_name = brand
                self.model_name = model
                self._price = max(price,0)
            
            
            def complete_info(self):
              return f"{self.brand_name} {self.model_name} and price is : {self._price}"  


            def call_phone(self,ph_no):
                print(f"calling {ph_no}.....")
            
class Smartphone(Mobile):        #derived class
    def __init__(self,brand,model,price,ram,i_memory,rear_cam):

      #  Mobile.__init__(self,brand,model,price):    #uncommon way
        super().__init__(brand,model,price)
        self.ram = ram 
        self.i_memory = i_memory
        self.rear_cam = rear_cam

class Tab(Smartphone):
        def __init__(self,brand,model,price,ram,i_memory,rear_cam,lock_type):
            super().__init__(brand,model,price,ram,i_memory,rear_cam) 
            self.lock_type = lock_type
        
        
        def complete_info(self):    #overriding of 
              return f"{self.brand_name} {self.model_name} {self.ram} {self.i_memory} {self.rear_cam} {self.lock_type} and price is : {self._price}"  
m1 = Mobile("samsung","s8",50000)
t1 = Tab("samsung","s8",50000,"8 GB","128 GB","25 px","eye_lock") 
# print(t1.complete_info())  
print(isinstance(t1,Mobile))       #print(help(Tab)) not working.......tab obj is automatically obj of mobile & smartphone class but not reverse.........
print(issubclass(Mobile,Tab))    #derived class,base class
print(Tab.__mro__)          #for inheritance order.....