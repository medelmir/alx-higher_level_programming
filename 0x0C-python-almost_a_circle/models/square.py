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
            self.id, self.x, self.y, self.width

    @property
    def size(self):
        """Get/set the size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value)
