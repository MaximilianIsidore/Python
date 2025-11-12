from itertools import groupby

def isContains_A(st):
    return 'a' in st

words =  ["hello", "ancient", "nile", "nest", "mountain"]

grp = groupby(words, key=isContains_A)

for key,value in grp:
    print(key, list(value))
