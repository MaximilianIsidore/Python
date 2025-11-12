
from itertools import permutations

a = [1,2,3]

perm = permutations(a,2)
print(list(perm))

from itertools import combinations

comb = combinations(a,2)
print(list(comb))