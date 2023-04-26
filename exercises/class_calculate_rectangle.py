"""
Write a class called Rectangle that contains the base and height,
and a method that returns the area of the shape.
"""


class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height


base = float(input("Enter the base of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

rectangle = Rectangle(base, height)
print("The area of the rectangle is:", rectangle.calculate_area())
