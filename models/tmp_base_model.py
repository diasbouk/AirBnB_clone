from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    # BaseModel class for all other classes
    #     in tht project
    def __init__(self, *args, **kwargs):
        # Class constructor
        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if kwargs == {}:
            models.storage.new(self)

    def __str__(self):
        # String representation of the instance
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Saves the current changes
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        # Returns dict of the class
        old_dict = self.__dict__
        new_dict = {}
        for key in old_dict.keys():
            new_dict[key] = old_dict[key]
        new_dict["__class__"] = str(self.__class__.__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
