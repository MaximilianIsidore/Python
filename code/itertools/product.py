
from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b)

print(list(prod))

c = [1,2]
d = [3]

prod = product(c,d, repeat=2)

print(list(prod))