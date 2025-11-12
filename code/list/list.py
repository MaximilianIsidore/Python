#list - ordered, mutable , allows duplicate elements, allows different types

fruits = ["Banana", "Apple", "Orange", "Pine Apple"]
print(fruits)

alltypes = [6, True, False, "String"]
print(alltypes)

#using loops

for i in alltypes:
    print(i)

#finding length
print(len(fruits))

fruits.append("berry")
print(fruits)

fruits.remove("Apple")
print(fruits)

#create list with specific element
zeros = [0] * 10
print(zeros)

#slice
print(fruits[1:])
print(fruits[:-1])
print(fruits[::-1])

#copy

list_og = [1,2,3,4,5]
list_dup = list_og.copy() #list_og[:] or list(list_og) also works, but assiging directly list_og create copy of memory not whole list

squared_num = [i*i for i in list_dup]