# def cube(n):
#     cubes={}
#     for i in range(1,n+1):
#         cubes[i] = i**3
#     return cubes
# print(cube(5))

# def word_count(string):
#         counter={}
#         for char in string:
#                 counter[char] = string.count(char)
#         return counter
# print(word_count("umanga"))
user = {}
fav_lan=input("your fav language seprated by comma").split(",")
user["fav_lan"] = fav_lan
print(user)    
