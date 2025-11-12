
def dec(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

def print_name():
    print("Max")

print_name = dec(print_name)

print_name()


def set_dec(func):

    def wrapper(*args, **kwargs):
        print("adding")
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper

@set_dec
def add10(a):
    return a+5

print(add10(10))