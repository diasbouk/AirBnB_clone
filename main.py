#!/usr/bin/python3

from models import base_model
from models.base_model import BaseModel

class test:
    pass
print(test.__dict__)

my_model =BaseModel()
print(my_model.__dict__)

print(my_model.__dict__["name"])
# print(my_model.__dict__[0])
# print(my_model.__dict__[0])
# print(my_model.__dict__[0])
