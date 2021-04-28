#enumerate function............
# names = ["umang","patel","chintu"]

# def pos_find(names,find_name):
#     for pos , name in enumerate(names):
#         if name == find_name:
#             return pos 
#     return -1
# print(pos_find(names,"patel"))

#map function.....(use for in-built function..like len...)
# last_char = list(map(lambda name : name[-1] , names))
# print(last_char)

# length = map(len,names)
# for i in length:
#         print(i)

#filter_funnction......

numbers=[1,2324,54,43,2]
even = list(filter(lambda no :  no % 2 == 0,numbers))
print(even)