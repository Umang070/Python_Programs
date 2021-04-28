#GENERATORS ARE ITERATORS............

#memory ---------- [---------------] ......list [save in memory]
#memory ---------- [----].......generators[at a time one] memory space reduce and perforamnce is better
# import time
# t1 =time.time()
# def nums(n):
#     for i in range(1,n+1):
#         yield i
# temp = nums(10)
# for i in temp:
#     print(i)
# t2 =time.time()
# print((t2-t1))

def even_no(n):
    for i in range(2,n+1,2):
        yield i
    
temp_e=even_no(5)
for i in temp_e:        # if i write for i in even_no(4): then two time loop execute....
    print(i)


    