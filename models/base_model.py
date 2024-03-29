#!/usr/bin/python3
<<<<<<< HEAD
"""
Base model for all classes
"""

import uuid
import datetime
import json
from datetime import datetime


class BaseModel:
    """
    Base model
    """

    def __init__(self, *args, **kwargs):
        """
        Init methode of our object

        Args:
             *args: Additional positional arguments (if any).
             **kwargs: Additional keyword arguments (if any).

         Attributes:
             id (str): The unique identifier of the object.
             created_at (datetime): time when has been created
             updated_at (datetime): time when has been updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            for key in kwargs:
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"
                )
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Class string presentation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the time to last update
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Saves class info into a dictionary
        """
        class_dict = {}
        for element in self.__dict__:
            class_dict[element] = self.__dict__[element]
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
=======
from uuid import uuid4
>>>>>>> Enissay
