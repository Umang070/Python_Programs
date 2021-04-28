# def fun(**kwargs):
#     for key,val in kwargs.items():
#             print(f"{key} : {val}")
# fun(first_name = "umang" , last_name = "patel")

#PADK---->parameter,args,default,kwargs...

# def fun_1(name,*args,age='none',**kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
# l=[1,2,3]
# d={'a':1,'b':2}
# fun_1("umang",*l,**d)

names = ["umang" , "patel"]

def funn(l,**kwargs):
    if kwargs.get('reverse_str') == True:
            return [name[::-1].title() for name in l]
    else:
            return [name.title() for name in l]
print(funn(names,reverse_str = True))