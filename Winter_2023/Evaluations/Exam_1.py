"""
Question 1. 
"""
from math import *

# TODO Answer question 1 below

# a) False
# b) True
# c) False
# d) True
# e) True
# f) True
# g) True
# h) False

"""
Question 2:
"""

# TODO Answer question 2 below


def is_triangle(a, b, c):
    if min(a, b, c) <= 0:
        raise ValueError("Values must be positive integers.")
    return a + b > c


print(is_triangle(1, 2, 3))

"""
Question 3:
"""

# TODO Answer question 3 below


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = int(length)
        self.width = int(width)

    def area(self):
        area = (self.length * self.width)
        return area

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter

    def is_square(self):
        if self.length == self.width:
            return True
        else:
            return False


rec = Rectangle(2, 4)
print(rec.area())
print(rec.perimeter())
print(rec.is_square())

"""
Question 4
"""

# TODO Answer question 4 below


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def display_position(self):
        return f"({self.x},{self.y})"


p1 = Point(1, 4)
p2 = Point(1, 5)

print(f"Distance p1-p2 is: {p1.distance(p2)}")

p1.move(0, 1)

print(f"After moving, the distance p1-p2 is: {p1.distance(p2)}")

print(f"Position of p1: {p1.display_position()}")
print(f"Position of p2: {p2.display_position()}")
