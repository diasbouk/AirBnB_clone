#!/usr/bin/python3
# Import modules and stuff here

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    Public class attributes:

        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
