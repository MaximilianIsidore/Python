
from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)

print(list(acc))

import operator

mul_acc = accumulate(a, func=operator.mul)
print(list(mul_acc))

print(list(acc))