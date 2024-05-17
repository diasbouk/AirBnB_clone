#!/usr/bin/python3

from models import base_model
from models.base_model import BaseModel

# class test:
#     pass
# print(test.__dict__)

my_model =BaseModel()
# print(my_model.__dict__)



print(my_model.__str__)
print("--------")
print(my_model)
print("--------")
print(type(my_model))
print("--------")

my_model.number =  1111

for key in my_model.__dict__:
    print("{}==> ".format(key), end="")
    print("{}".format(my_model.__dict__[key]))
# print(my_model.__dict__[0])
# print(my_model.__dict__[0])
# print(my_model.__dict__[0])
