import os
from typing import List

"""
1. Create a Person class with the attributes last_name, first_name, and age.
Ensure that age is a positive integer.
Otherwise, raise an error.
Write a method display_details that displays the person's details.
"""


class Person:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        if age >= 0:
            self.age = age
        else:
            raise ValueError("Age must be a positive integer")

    def display_details(self):
        print(f"Last name: {self.last_name}, First name: {self.first_name}, Age: {self.age}")


# John = Person('Doe', 'John', 5)
# John.display_details()

"""
2. Create a BankAccount class with the attributes name and balance.
Ensure that the balance is a positive number.
Write methods to deposit and withdraw money.
Write a method to display the person's balance.
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        if balance < 0:
            raise Exception("Balance must be greater than 0")
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            raise Exception("Insufficient balance")

    def display(self):
        print(f"Hello {self.name}. Your balance is {self.balance}")


# accountJohn = BankAccount("John", 20)
# #accountJohn.display()
# accountJohn.deposit(50)        
# accountJohn.withdraw(60)
# accountJohn.display()

"""
Create a Rectangle class with the attributes length and width.
Ensure that length and width are positive numbers.
Otherwise, raise an exception.
Write a method to calculate the area of the rectangle. This method returns the area.
Write a method to calculate the perimeter of the rectangle. This method returns the perimeter.
Write a method to display the area of the rectangle.
Write a method to display the perimeter of the rectangle.
"""


class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise Exception("Length and width must be positive")

        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        return perimeter

    def display_area(self):
        print(f"The area is {self.calculate_area()}")

    def display_perimeter(self):
        print(f"The perimeter is {self.calculate_perimeter()}")


# rectangle1 = Rectangle(27, 2)
# rectangle1.display_area()
# rectangle1.display_perimeter()

"""
4. 
    Create a Student class with the attributes 
    last_name: str,
    first_name: str,
    id: int,
    courses: List[str]. 
    Ensure that the ID is a positive number.
    Write a method to add courses.
    Write a method to remove courses.
    Write a method to display the enrolled courses.
"""


class Student:
    def __init__(self, last_name: str, first_name: str, id: int, courses: List[str]):
        self.last_name = last_name
        self.first_name = first_name
        if id > 0:
            self.id = id
        else:
            raise ValueError("ID must be positive")
        self.courses = courses

    def add_course(self, course: str):
        self.courses.append(course)

    def remove_course(self, course: str):
        self.courses.remove(course)

    def display_courses(self):
        print("Enrolled courses:")
        for c in self.courses:
            print(c)


# Alex = Student("Smith", "Alex", 2, [])
# Alex.add_course("Programming")
# Alex.add_course("Music")
# Alex.add_course("Science")
# Alex.add_course("Linux")

# Alex.remove_course('Music')
# Alex.display_courses()

"""    
    5. Create a Car class with the attributes brand, model, year, and mileage.
    Ensure that year and mileage are positive numbers.
    Write a method to display the car details.
"""


class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: int):
        self.brand = brand
        self.model = model
        if year <= 0 or mileage <= 0:
            raise ValueError("Year must be positive")
        self.year = year
        self.mileage = mileage

    def display_details(self):
        print(
            f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage:,} km\n")


# car_1 = Car("Lamborghini", "Gallardo", 2011, 80000)
# car_2 = Car("Ferrari", "Enzo", 2001, 24000)
# car_1.display_details(), car_2.display_details()

"""    
    6. Create a File class with the attributes name and content.
    Write a constructor that takes the file name and content as input,
    and a method to display the file content.
    Also, write a method to delete the file when the object is destroyed.
"""


class File:
    files = []

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def display_content(self):
        try:
            with open(self.name, 'r') as file:
                content = file.read()
                print(f"Content of file {self.name}:")
                print(content)
        except FileNotFoundError:
            print(f"The file {self.name} does not exist.")

    @classmethod
    def create_file(cls, *files):
        for file in files:
            if os.path.exists(file.name):
                print(f"The file {file.name} already exists.")
            else:
                try:
                    with open(file.name, 'w') as f:
                        f.write(file.content)
                    cls.files.append(file.name)
                except Exception as e:
                    print(f"Error creating the file {file.name}: {e}")

    @classmethod
    def display_all(cls):
        print("List of all created files:", ', '.join(cls.files))

    def __del__(self):
        try:
            os.remove(self.name)
            print(f"The file {self.name} has been successfully deleted.")
        except FileNotFoundError:
            print(f"The file {self.name} does not exist.")

# Example usage
file1 = File("cat.jpeg", "Image of a cat.")
file2 = File("different_cat.png", "Different image of a cat")
file3 = File("song.mp3", "Different cat sounds")
File.create_file(file1, file2, file3)
File.display_all()
