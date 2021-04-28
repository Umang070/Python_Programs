# neg_num = [ -i for i in range(1,11) ]
# print(neg_num)
# names = ["umang","patel","chintu"]
# names = [name[0] for name in names]
# print(names)
# new_names = [name[::-1] for name in names]
# print(new_names)

#WITH IF STATEMENT....


# odd_nums = [i for i in range(1,11) if i % 2  != 0]
# print(odd_nums)

# def num_to_string(l):
#     return [str(i) for i in l if type(i) == int or type(i) == float]
# print(num_to_string([1,2,3,"umang",[1,2]]))

#using all--->
# if all([(type(arg) == int or type(arg) == float) for arg in args]):
#print(my_sum(1,3,4,"umang",4.3))
#with if else .....

# nums = [1,2,3,4,5]
# new_nums = [i*2 if (i % 2 == 0) else -i for i in nums]
# print(new_nums)

#nestes list...

# ex = [[1,2,3],[1,2,3],[1,2,3]]
new_ex =[[i for i in range(1,4)] for j in range(4)] #if i want 1,2,3    4,5,6   7,8,9 ...??
print(new_ex)