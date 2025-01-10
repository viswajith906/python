class Rectangle:
    def __init__(self, length, width):  # Corrected the constructor method
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)  # Removed extra space between class and parameters

print("Area of the rectangle:", rectangle.calculate_area())
print("Perimeter of the rectangle:", rectangle.calculate_perimeter())