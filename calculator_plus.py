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
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(x)

class GeometryCalculator:

    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return math.pi * radius ** 2

if __name__ == "__main__":
    calculator = Calculator()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print(f"{num1} + {num2} = {calculator.add(num1, num2):.2f}")
        print(f"{num1} - {num2} = {calculator.subtract(num1, num2):.2f}")
        print(f"{num1} * {num2} = {calculator.multiply(num1, num2):.2f}")

        try:
            print(f"{num1} / {num2} = {calculator.divide(num1, num2):.2f}")
        except ValueError as e:
            print(e)

        num3 = float(input("Enter a number to find its square root: "))
        try:
            print(f"The square root of {num3} = {calculator.square_root(num3):.2f}")
        except ValueError as e:
            print(e)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    geometry_calculator = GeometryCalculator()

    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle = {geometry_calculator.calculate_rectangle_area(length, width):.2f}")

        radius = float(input("Enter the radius of the circle: "))
        try:
            print(f"The area of the circle = {geometry_calculator.calculate_circle_area(radius):.2f}")
        except ValueError as e:
            print(e)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
