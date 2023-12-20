# This principle states - Software entities (classes, modules, functions, etc.) should be open for extension, 
# but closed for modification.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return pi * self.radius**2
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def area(self):
        return self.side**2

# Shape class provides the required interface (API) for any shape that you’d like to define.
# It closes the class to modifications. 
# Now you can add new shapes to your class design without the need to modify Shape. (As Circle and Square in example)
