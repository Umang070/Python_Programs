from functools import wraps

def only_string(data_type):
    def decorator(any_function):
        @wraps(any_function)
        def inside_fun(*args,**kwargs):
                if all([type(arg) == data_type for arg in args]):
                    return any_function(*args,**kwargs)
                print('invalid input')
        return inside_fun
    return decorator

@only_string(str)
def only_string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

l = ["umang","patel","7070"]
print(only_string_join(*l))