#!/usr/bin/python3
"""This is the BaseModel module"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The class BaseModel defined"""
    def __init__(self, *args, **kwargs):
        """Initialization of Attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                setattr(self, key, val)

    def __str__(self):
        """Returns the string representation"""
        c_name = "[{}] ({}) {}"
        return c_name.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attr with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary having all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
