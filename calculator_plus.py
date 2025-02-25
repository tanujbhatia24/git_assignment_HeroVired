import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)
        
class GeometryCalculator:
       
    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

if __name__ == "__main__":
    
    calculator = Calculator()
    num1 = 16
    num2 = 4
    num3 = 25

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
    print(f"The square root of {num3} = {calculator.square_root(num3)}")
    
    calculator = GeometryCalculator()
    length = 10
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")

    radius = 5
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")
