from uuid import uuid4
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    # BaseModel class for all other classes
    #     in tht project
    def __init__(self, *args, **kwargs):
        # Class constructor
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "create_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        if kwargs == {}:
            storage.new(self)

    def __str__(self):
        # String representation of the instance
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Saves the current changes
        self.updated_at = datetime.now()
        storage.save()

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
