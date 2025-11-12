import random

a = random.random()
print(a)

a = random.randint(1, 10)
print(a)

#create a same sequence
random.seed(1)

a = random.random()
print(a)

random.seed(1)
a = random.random()
print(a)

#true random numbers
import secrets

a = secrets.randbits(4)#4 bit -1111 = 15
print(a)

#filling array, matrix with random numbers

import numpy as np

a = np.random.rand(3,3)
print(a)


