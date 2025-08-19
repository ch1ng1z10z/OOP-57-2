
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase
def say_hello():
    return "вы слышали это да? это шелчок моего вальтера, он нацелен на ваши яйца"


print(say_hello())



