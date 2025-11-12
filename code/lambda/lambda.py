
add = lambda x,y  : x+y

print(add(5,6))

points2D = [(1,2), (15,-1), (4,12), (10,1)]
points2D_sorted = sorted(points2D)

print(points2D_sorted)

points2D_sorted = sorted(points2D, key = lambda x : x[1])
print(points2D_sorted)

#map

a = [1,2,3,4]
b = map(lambda x:x*2, a)

print(list(b))

#filter

c = filter(lambda x : x%2 == 0, a)

print(list(c))

#reduce
from functools import reduce

b = reduce(lambda x,y : x*y, a)
print(b)