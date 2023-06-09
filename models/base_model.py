#!/usr/bin/python3
""" class BaseModel that defines all common
    attributes/methods for other classes
"""
import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """class constructor
        re-creates an instance from a dictionary representation,
        else creates a new instance.
        The unique id should be converted to a string.
        """

        if kwargs:
            for attr in kwargs:
                if attr == "created_at" or attr == "updated_at":
                    dtf = "%Y-%m-%dT%H:%M:%S.%f"
                    val = datetime.strptime(kwargs[attr], dtf)
                    kwargs[attr] = val
                if attr != "__class__":
                    setattr(self, attr, kwargs[attr])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of an instance. A key __class__ must be added to this dictionary
        with the class name of the object. created_at and updated_at must
        be converted to string object in ISO format
        """
        a_dict = self.__dict__.copy()
        a_dict["__class__"] = self.__class__.__name__
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        return a_dict
