# c,c++,java-----array[only one datatype store]
# python array module -->fixed datatype]
# list----->flexible[store any datatype] we use list or NUMPY array -- binding c
# sting are immutable[do not change in original string]
# # lists are mutable
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for sublist in matrix:
#         for i in sublist:
#                 print(i,end=" ")
# print(type(matrix))
words=["abc","xyz","pqr"]


def reverse_ele(r):
    elements = []
    for i in r:
        elements.append(i[::-1])
    return elements
print(reverse_ele(words))




# no=list(range(1,11))
no=[1,2,3, 4, 5, 6, 7, 8, 9, 10,1]
# print(no)
# print(no.index(1,3,10)) #1 , start , stop
def negative_no(neg):
    negative=[]
    for i in neg:
                negative.append(-i)
    return negative
print(negative_no(no))