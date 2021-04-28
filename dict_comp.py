# sq = {(f"square of {num} "): num ** 2 for num in range(1,5)}
# for i,j in sq.items():
#         print(f"{i} : {j}")

# def word_count(name):
#     return { char : name.count(char) for char in name}
# print(word_count("umang"))

# o_e = {i : ('even' if i %2 == 0 else 'odd') for i in range(1,11)}
# print(o_e)
max_no = int(input("enter a number: "))
# prime = {i : ('not prime' if max_no % i == 0 else 'prime')for i in range(2,max_no)}
# print(prime)

k=0 
for i in range(2,max_no):
        if max_no % i == 0:
            k=k+1
if (k==0):
    print("number is prime")
else:
    print("number is not prime")