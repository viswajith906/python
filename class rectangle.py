class Rectangle:
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width  # Private attribute

    def area(self):
        return self.__length * self.__width  # Corrected to use __length and __width

    def __lt__(self, other):
        return self.area() < other.area()

# Input for both rectangles
length1 = float(input("Enter the length of Rectangle 1: "))
width1 = float(input("Enter the width of Rectangle 1: "))

length2 = float(input("Enter the length of Rectangle 2: "))
width2 = float(input("Enter the width of Rectangle 2: "))

# Create two rectangle objects
rect1 = Rectangle(length1, width1)
rect2 = Rectangle(length2, width2)

# Compare areas using the overloaded < operator
if rect1 < rect2:
    print("Rectangle 1 has a smaller area than Rectangle 2.")
else:
    print("Rectangle 1 has an area greater than or equal to Rectangle 2.")