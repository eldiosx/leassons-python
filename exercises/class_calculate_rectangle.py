"""
Write a class called Rectangle that contains the base and height,
and a method that returns the area of the shape.
"""

#create class for the figure
class Rectangle:
    #part of the data, for other figures more may be required
    def __init__(self, base, height):
        self.base = base
        self.height = height
    #you can modify these formula for another figure
    def calculate_area(self):
        return self.base * self.height

#console data entry
base = float(input("Enter the base of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

rectangle = Rectangle(base, height)
#print by console
print("The area of the rectangle is:", rectangle.calculate_area())
