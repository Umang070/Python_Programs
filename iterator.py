# numbers = [1,2,3,4] #tuples,string------iterables...
# number_iter = iter(numbers)
# print(next(number_iter))

numbers=[2,4,6,5,8]
print(all([ num % 2 == 0 for num in numbers ])) #all means check all value are true or not....
print(any([ num % 2 == 0 for num in numbers ])) #all means check any value are true or not....