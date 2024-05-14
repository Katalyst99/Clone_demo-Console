#!/usr/bin/python3
"""This is the BaseModel module"""

import uuid
from datetime import datetime


class BaseModel:
    """The class BaseModel defined"""
    def __init__(self):
        """Initialization of Attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation"""
        c_name = "[{}] ({}) {}"
        return c_name.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attr with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary having all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

model = BaseModel()
print(model)

