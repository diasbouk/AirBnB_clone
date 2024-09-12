#!/usr/bin/python3

"""
    The Base model that all other modules of the project will inherite
    uuid: To generate uuid4 unique ids for each instance
    datetime: To assign each instance with it's creation and update time
        using the datetime.now() method
    models: Modules of our project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The Base class of all other models"""

    def __init__(self, *args, **kwargs):
        """
        __init__: Our class constructor
        args: Arguments as strings to create instance
        kwargs: Dict with attributes to create or recreat
        and existing instane
        """
        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if kwargs == {}:
            models.storage.new(self)

    def __str__(self):
        """__str__: returns a string
        returns the string repr of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        save: The save method
        saves the current instance
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """to_dict method
        returns a dictionary holding all instance
        attributes and their values att->val
        """
        old_dict = self.__dict__
        new_dict = {}
        for key in old_dict.keys():
            new_dict[key] = old_dict[key]
        new_dict["__class__"] = str(self.__class__.__name__)
        new_dict["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict["updated_at"] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return new_dict
