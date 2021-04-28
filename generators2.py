#convert list comprehension to generator comprehension.........
# cube = (i ** 3 for i in range(1,20))
# print(next(cube))
# print(next(cube))
import time
t1 = time.time()
cube = [i ** 3 for i in range(1000000)]
print(time.time()-t1)
# cube = (i ** 3 for i in range(100000000))
