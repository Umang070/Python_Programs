# unordered collections of data in key : value pair.

user = {'name' : "umang", 'age':19,'fav_movies' : ["3 idiots","dhamal"]}
# user = dict( name ="umang", age=19)
# print(user)
# print(user['name'])
if 'umang' in user.values():
            print("present")
else :
            print("not present")
# numbers ,,,,, string,,,list can be added in dict.
# user_i = {}
# user_i['number'] = 20
# print(user_i)

for i in user.values():
            print(i)
for key,val in user.items():
            print(f"key is : {key} and value is : {val}")