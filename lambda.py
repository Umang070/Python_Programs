from functools import reduce
# mul = lambda a,b : a * b
# print(mul(2,3))
# print(mul)

# rev_string_with_capital_char= lambda s : s[::-1].title()
# print(rev_string_with_capital_char("umang"))
numbers=[1,2,3,4]
# is_even = list(map(lambda no : 'Even' if no % 2 == 0 else 'Odd',numbers))
is_ev = list(filter(lambda a : a% 2 == 0,numbers))
print(is_ev)
sum = reduce(lambda a,b : a+b,is_ev)
print(sum)
#without map and filter not use sequence list.......with lambda 