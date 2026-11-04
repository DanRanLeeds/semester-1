# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance(width, (int)) or not isinstance(height, (int)):
            raise TypeError("Parameters can only be integers")
        if width <= 0 or height <= 0:
            raise ValueError("Parameters must be positive integers")
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        if self.width == self.height:
            return True
        else:
             return False
    
    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.width +self.height) + (self.width + self.height)
        return perimeter
    
    
Rectangle1 = Rectangle(0,3)
print(Rectangle1.is_square())
print(Rectangle1.area())
print(Rectangle1.perimeter())