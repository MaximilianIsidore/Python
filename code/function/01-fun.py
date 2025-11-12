def get_name(name):
    return f"Hello {name}"

def greet(name):
    msg = get_name(name)
    print(msg," how are you?")

name = input("Enter the name: ")

greet(name)