# def odd_even(l):
#     odd_number=[]
#     even_number=[]
#     for i in l:
#             if i % 2 == 0:
#                 even_number.append(i)
#             else : 
#                 odd_number.append(i)
#     output = [odd_number,even_number]
#     return output
# numbers=[1,2,3,4,5,6,7,8]
# print(odd_even(numbers))
def common(l1,l2):
    output = []
    for i in l1:
            if i in l2:
                        output.append(i)
    return output
num1 = [1,2,3,4]
num2 = [2,3,5]
print(common(num1,num2))