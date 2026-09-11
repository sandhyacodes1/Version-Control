def my_decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
        print("Goodbye!")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")
greet("Sandhya")