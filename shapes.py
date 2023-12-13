import math

#Area of a circle
radius = input("Enter the radius of a the circle: ")
circle_area = math.pi * int(radius) ** 2
print(f"The area of the circle with a radius of {radius} is: {circle_area} ")

#Area of a triangle
base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")
triangle_area = int(base) * int(height)
print(f"The area of the triangle with base {base} and height {height} is: {triangle_area}")

#Area of a rectangle
length = input("Enter the length of the rectangle: ")
breadth = input("Enter the breadth of the rectangle: ")
rectangle_area = int(length) * int(breadth)
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {rectangle_area}")
