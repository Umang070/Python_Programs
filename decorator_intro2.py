# @ use for decorator.. syntetic sugar..........
import time
from functools import wraps #for doc lines....

def decorator_fun(any_func):
    @wraps(any_func)
    def inside_fun(*args,**kwargs):
        """this is doc line of inside funnction"""
        
        t1 = time.time()
        print(f"starting time for execution is {t1} second")
        print(f"this is call {any_func.__name__} function")                                            #print(inside_fun.__doc__) i want to print doc line of inside func..
        print(f"doc linne of add fun is {any_func.__doc__}")
        print("this is decorator function")
        return_val = any_func(*args,**kwargs)       #b'caz we calcute execution time too....
        t2 = time.time()
        print(f"last time for execution is {t2} second")
        print(f"time taken for execution is : {t2-t1} second")
        return return_val
    return inside_fun

# ---------------1)-----------------
# @decorator_fun      #shortcut.....
# def fun1():
#      print("this is function 1")
# temp = decorator_fun(fun1)  shortuct or this...............
# print(temp())

# ---------------2)-----------------
@decorator_fun  
def fun1(a):            #we can pass multiple value ????? with out args
        """ take a one argument"""
        print(f"this is function 1 with argument {a}")
fun1(3)

# ---------------3)-----------------
# @decorator_fun
# def mul(no1,no2):
#         return no1 * no2
# print(mul(2,3))

