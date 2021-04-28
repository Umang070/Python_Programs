# numbers = [23,454,3]
# print(max(numbers))

# def greatest_diff(l):
#     return max(l) - min(l)

# print(greatest_diff(numbers))
#  n=[[1,12],[12,34],[323,4]]

# def count_list(l):
#             count = 0
#             for i in l:
#                     if type(i) == list:
#                         count += 1
#             return count
# print(count_list(n))
# name=["umang","vicky","rakeshbhai"]
# print(min(name,key = lambda item : len(item)))  #if both len same how decide umang is min..........????

#advance sort........

bikes = [ 
            {
                'model' : 'gixxer' , 'price' : 100000},
            {   'model' : 'bulet'  , 'price' : 150000},
            {    'model' : 'pulsar'  , 'price' : 50000}
        ]
print(sorted(bikes , key = lambda d: d.get('price'),reverse = True))