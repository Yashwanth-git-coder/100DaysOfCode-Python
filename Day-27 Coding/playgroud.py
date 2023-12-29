#*args

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#
# add(1,3,45,3,5,2)

# def calculcate(n, **kwargs):
#     print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculcate(2, add = 3, multiply = 5)

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")
#
# my_car = Car(make="Nissan", model="Skyline")
# print(my_car.colorf)

# def test(*args):
#     print(args)
#
#
# test(1, 2, 3, 5)

def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)