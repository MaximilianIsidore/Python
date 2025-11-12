
from collections import namedtuple

point = namedtuple('Point','x,y') #creates a class named point with tuple values x, y

pt1 = point(5,10)
print(pt1)