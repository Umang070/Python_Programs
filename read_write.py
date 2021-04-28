f = open("file.txt")
# print(f"cursor positon = {f.tell()}")
# print(f.read()) #do not do for 2 times
# print(f"cursor positon = {f.tell()}")
# print("befor seek method")
# f.seek(0)
# print("after seek method")
# print(f"cursor positon = {f.tell()}")
# print(f.read())
# print(f.readline(),end = "")
# lines = f.readlines()
# print(len(lines))   #no of lines
# for line in lines:     or.......... for line in f
#         print(line,end="")
# print(f.name) # for file name data discripter
#print(f.closed) # file close or not..........
# f.close()

#----------with block-------------
#--------context manager------------

# with open("file.txt") as f:
#     data = f.read()
#     print(data)

# with open("file2.txt","w") as f: #w means overrite data...and if file not then it is create
#     f.write("welcomme")

# with open("file2.txt","a") as f: # means print after our data
#      f.write("\nafter our data")


# with open("file2.txt","r+") as f: # means read or write and jetlu lkhyu te size erase karse
#     f.seek(len(f.read()))
#     f.write("\nnever give up\n")

# with open("filename_read.txt","r") as rf:
#     with open("filename_write.txt","w") as wf:
#         wf.write(rf.read())