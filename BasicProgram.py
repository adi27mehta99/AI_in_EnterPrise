def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"

name = input("Enter your name: ")
print(greet(name))
