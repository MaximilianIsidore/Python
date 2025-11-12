
from collections import Counter

a = "abcabcetygfdrreth"

count = Counter(a)#converts to dictionary format

print(count)
print(count.most_common(2))

print(count.most_common(3)[1])