from uuid import uuid4
from datetime import datetime

class BaseModel:
    # BaseModel class for all other classes
    #     in tht project
    def __init__(self):
        # Class constructor
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        # String representation of the instance
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}" 
    def save(self):
        # Saves the current changes
        self.updated_at = datetime.now()
    def to_dict(self):
        # Returns dict of the class
        return (self.__dict__)

