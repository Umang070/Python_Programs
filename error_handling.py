#try except else finally.....
# while True: #infinite loop.....
#     try:
#         age = int(input("enter your age"))    #.......seven
#         print(f"user input is : {age} ")
#         break
    
#     except ValueError as err:      #not correct datatype:
#         #print("may be u enter string insted of number........") user msg
#         print(err)      #means automatic msg print
     
#     except ZeroDivisionError as zr:
#         print("NOT DIVIDE BY ZERO",zr)
#     except Exception as e: # if any other error....
#         print("unexpected error")
    
#     else:
#         print(f"user input is : {age} ")    # if not any exception......
#         break
#     finally:
#         print("finally block............called")    #if error is come or not this is always called.....database code.etc..


# if age > 18 :
#         print("valid")
# else: 
#         print("not")

# custom exception ---------to increase redability of code.....


class NameTooLongError(ValueError):     #own exception.........
    pass

def valid(name):
    if len(name) < 6:
            print(f"your name is {name}")
    else:       
        raise NameTooLongError("name is too long")
print(valid("umangpatel"))