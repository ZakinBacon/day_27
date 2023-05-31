import tkinter

def add(*args):
    total = 0
    for x in args:
        total += x
    return total


print(add(3, 5, 6, 8))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # the get feature return NA instead of erroring out
        self.make = kwargs.get("make")
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)