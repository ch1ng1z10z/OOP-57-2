
def uppercase(func):
    def fg():
        for i in func:
            fg(i.upper())


@uppercase
def say_hello():
   return "hello, world"



