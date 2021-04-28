# def all_total(*args):   #we can pass any number of numbers.....
#     total = 0
#     for num in args:
#         total += num
#     return total
                        
# print(all_total(1,2,3))    #type is tuple

#args with noraml parameter

# def is_mul(num,*args):
#     mul = 1
#     for i in args:
#             mul = mul * i
#     return mul
# print(is_mul(3,2,3))    #first parameter treat as a noraml...

# args as a argument...

# def is_mul(*args):
#     mul = 1
#     # print(args)
#     for i in args:
#             mul = mul * i
#     return mul
# nums=[1,2,3,4]
# print(is_mul(*nums))   #unpack....

def to_power(num,*args):
    if args:                                    #if list:  means list is not contain enything it is go to else part.....
            return [i ** num for i in args]
    else:
            print("u did'nt pass args:")
nums=[3,4]
print(to_power(2,*nums))