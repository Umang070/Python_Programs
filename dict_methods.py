user = {'name' : "umang", 'age':19,'fav_movies' : ["3 idiots","dhamal"]}
# user['fav_song'] = ['song1','song2']
# print(user)
# pop_items=user.pop('fav_movies')   # pop_items=user.popitem()    
# print(f"delete values are : {pop_items}")
# print(user)
# add={'fav_color': ['black','purple']}
# user.update(add)
# print(user)



# detail = dict.fromkeys(['name','age'],'unknown')    #("abc","unknown") (range(1,11),"unknown")
# print(detail)

# GET METHOD..
print(user.get('names','not found!!'))   #user['name']
# if user.get('name'):
#         present....

#COPY
user_info=user.copy()
print(user_info.popitem())
print(user)
print(user_info is user)