# This principle states - Subtypes must be substitutable for their base types.
# For example, if you have a piece of code that works with a Shape class, 
# then you should be able to substitute that class with any of its subclasses, 
# such as Circle or Rectangle, without breaking the code.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Now you can use the Shape type interchangeably with its Square and Rectangle subtypes when you only care about their common behavior
