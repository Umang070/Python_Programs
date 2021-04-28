s = {1,2,34,34,"umang",2}
s1 = {1,2,"umang",45,47}
 # print(s)
# l=[1,2,3,43,43,2,5,6]
# s=list(set(l))
print(s)
s.add(4)
# s.remove(3) #if it is not in set thenn throw error....
s.discard(4) #if it is not in set thenn do not throw error....
# print(s.clear())

# for i in s:
#         print(i)
union = s | s1
print(union)
intersection = s & s1
print(intersection)

