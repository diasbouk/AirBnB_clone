#!/usr/bin/python3

""" For import modules and stuff """

from models.base_model import BaseModel
import models


class User(BaseModel):
    """ User class that inherites from
    the BaseModel class
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
