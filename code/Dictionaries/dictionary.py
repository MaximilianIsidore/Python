#dictionary - unordered, mutable, key-value pair, key - unique

dict = {
    "name" : "mr",
    "address" : "unknown",
    "age" : "unknown"
}

print(dict)

dict["email"] = "thestranger@universe.com"
print(dict)

for (key, value) in dict.items():
    print(key,":", value)

del dict["age"]

print(dict)
