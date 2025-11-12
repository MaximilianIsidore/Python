
from collections import deque

d = deque()

d.append(1)
d.append(2)

print(d)

d.appendleft(3)
d.appendleft(0)
print(d)

d.extend([5,6,7])
print(d)

d.extendleft([-2,-3])
print(d)

d.rotate(1) #right
print(d)

d.rotate(-1) #left
print(d)