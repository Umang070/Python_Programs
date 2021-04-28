class Count:
            instance_count = 0
            def __init__(self,first,last,age):
                Count.instance_count += 1
                self.first = first
                self.last = last
                self.age = age
            @classmethod        #for define class methods .......use decorator...and cls point to class Count...
            def calculate_instance(cls):
                return f"you have created {cls.instance_count} instance of {cls.__name__} class"
            
            #class_methods as a constructor.....

            @classmethod
            def one_string(cls,string):
                first_name,last_name,age=string.split(",")  #not create obj
                return cls(first_name,last_name,age)        #obj created.....
            def full_name(self):
                return f"full name is {self.first} {self.last}"

            @staticmethod       #not connection to class or obj but logical connection to class.....
            def welcome():
                print("static method is called")
                
c1=Count("chintu","patel","18")

print(Count.calculate_instance())
c3 =Count.one_string('umang,patel,19')  #own constructor why need.....?
print(c3.full_name())
c3.welcome()










