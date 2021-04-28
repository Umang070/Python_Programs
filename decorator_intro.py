#def cube(no):
#   return no ** 3
# temp = cube
# print(temp.__name__)
# print(temp)
# print(cube) #temp and cube both are at same memory.

#FUNN AS  A ARGUMENT...........
# l=[1,2,3,4]
# def my_map(func,l):
#     return [func(item) for item in l]
#print(my_map(lambda no : no ** 3,l))  
# or......     
#print(my_map(cube,l)) 

#FUNCTION RETURNING FUNCTION(CLOSURE)...........

# def outer_fun(msg):
#     def innerr_fun():
#         print(f"message is {msg}")
#     return innerr_fun     #if we write () then means return after execute.........
# var = outer_fun("hello umang")
# var()

def power(p):
    def cal_power(no):
            return no ** p
    return cal_power
cube = power(3)
print(cube(3))

