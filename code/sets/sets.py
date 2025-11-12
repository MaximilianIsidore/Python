#sets - unordered, no duplicates, mutable

set1 = {1, 2, 4, 3, 1, 0}
print(set1)

str_set = {"hello"}
print(str_set)

str_set2 = set("hello")
print(str_set2)

set1.add(5)
set1.add(7)

set1.remove(1)

print(set1)

odd = {1,3,5,7,9}
even = {0,2,4,6,8}
prime = {2,3,5,7}

print(odd.union(even))
print(odd.intersection(prime))
print(odd.difference(prime))

print(even.symmetric_difference(prime))
