#!/usr/bin/python3
"""
This is the script for BaseModel Class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """ This class contains functionalities common to all
    other classes, from which they inherit.
    """

    def __init__(self):
        """This func initializes the instance attributes of the
        BaseModel class.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """This func returns the string representations
        of the objs
        """

        class_name = type(self).__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """This func updataes the pub instance attri 'updated_at'
        with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ This func returns as dict containing all keys/values-
        pairs of the __dict__ instance.
        """

        class_name = type(self).__name__
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = class_name
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return (my_dict)
