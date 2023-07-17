#!/usr/bin/python3
"""Defines a square model class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of this square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get/set the size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of this square."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
            return
        for attr, val in kwargs.items():
            setattr(self, attr, val)
