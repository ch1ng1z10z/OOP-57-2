
def uppercase(func):
    def wrapper(f):
        print(f.upper)
        func()
    return wrapper


@uppercase
def say_hello():
   return "hello, world"



