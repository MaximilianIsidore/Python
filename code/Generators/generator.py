
def my_generator():
    yield 1
    yield 2
    yield 3

print(my_generator)

#g = my_generator()
for o in my_generator():
    print(o)