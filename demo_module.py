def add():
    print("add",__name__)
def sub():
    print("sub")
def main():
    add()
    sub()
if __name__=="__main__":#if not write this then all time when import main is called even if we call only add..
   main()