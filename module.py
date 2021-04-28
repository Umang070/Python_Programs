from demo_module import add
def fun1():
    add()   #from demo_module so prinnt that name not __main__
    print("fun1")
def fun2():
    print("fun2")
def main():
    fun1()
    fun2()
main()