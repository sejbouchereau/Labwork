"""
1.
Create a Date class that represents a date (day, month, year).
Add methods to display the date in the format day/month/year and to determine if the year is a leap year.
display_date -> day/month/year
is_leap_year
Test your class by creating an instance of Date and displaying the date and whether the year is a leap year.
"""
from math import pi
from typing import List

"""
- If the day is not a number between 1 and 31, raise a ValueError
"""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        if 1 <= int(self.day) <= 31:
            self.month = month
            self.year = year
        else:
            raise ValueError('The day must be between 1 and 31')

    def display_date(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def is_leap_year(self):
        if self.year % 4 == 0:
            return True
        else:
            return False


# example = Date(6, "April", 2023)
# example.display_date()
# example.is_leap_year()


"""
Write a function that asks the user to enter a day, a month, a year, and returns a Date object. 
The function name is ask_for_date()

-- This function can return an error in three places:
    -- day = int(input)
    -- year = int(input)
    -- return Date(day, month, year)
--
    If an error is raised:
    I want to display on the screen: You have entered an invalid value along with the returned error. 
"""


def ask_for_date():
    try:
        day = int(input('Enter a day: '))
        month = input('Enter a month: ')
        year = int(input('Enter a year: '))

        return Date(day, month, year)
    except Exception as e:
        print(f"You have entered an invalid value. Here is the returned error: {e}")


date = ask_for_date()

if date.is_leap_year():
    print("The entered year is a leap year.")

yesterday = Date(5, 'April', 2023)
tomorrow = Date(7, 'April', 2023)
yesterday.display_date()
date.display_date()
tomorrow.display_date()

"""
Create a Book class that represents a book with a title, an author, and a price.
Add a method to return the book's title.
Add a method to return the book's author and 
a method to check if the book is on sale 
(that is, if the price is lower than a given price parameter).
"""

"""
In the is_book_on_sale method:
    -- If the given price parameter is greater than $35 
    -- Raise a ValueError saying: A sale price cannot be higher than $35
"""


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_title(self):
        print(self.title)

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def is_book_on_sale(self, price):
        if price > self.price:
            raise ValueError("A sale price cannot be higher than the item's price")
        return self.price > price


book = Book("Moby Dick", "Jules Verne", 60)

"""
I want to ask the user to enter a sale price
And I want to display Woohoo! if the book *Around the World in 80 Days* is on sale.

-- If this program returns a ValueError, display on the screen: You have entered an invalid value, followed by the returned error.
"""

try:
    sale_price = int(input("Enter the sale price: "))
    if book.is_book_on_sale(sale_price):
        print("Woohoo! You saved some precious money!")
    else:
        print("The book is not on sale")
except ValueError as e:
    print(f"You have entered an invalid value: {e}")

print(f"Thank you for your purchase: {book.get_title()} by {book.get_author()}.")

"""
Create a Student class that represents a student
with a first name: str, a last name: str, a birth date: Date, and a list of grades: List[int]. 
Add methods to 
calculate the student's grade average,
display their name, and
display their average.
"""


class Student:
    def __init__(self, first_name: str, last_name: str, birth_date: Date, grades: List[int]):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def display_name(self):
        print(f"{self.first_name} {self.last_name}")

    def display_average(self):
        print(self.calculate_average())


"""
I want to create an object with first name Jonathan, last name Joseph, birth date August 12, 1980, and grades [80, 79, 90, 58, 72]
"""

jonathan = Student('Jonathan', 'Joseph', Date(10, "July", 2000), [80, 79, 90, 58, 72])
jonathan.display_average(), jonathan.birth_date.display_date()

"""
Create a Circle class that has one attribute: the radius.
Add a method to calculate and return the area (pi*r^2) and another method to calculate the circumference (2*pi*r).
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_circumference(self):
        return 2 * pi * self.radius


circle_1 = Circle(10)
circle_2 = Circle(34)

print(int(circle_1.calculate_circumference()))
print(int(circle_2.calculate_circumference()))

"""
Create a CardGame class that has two attributes: 
the list of cards and 
a card is represented by an object of the Card class
which has 2 attributes: 
-- The value (number between 1 and 13)
-- The suit (Spade, Club, Heart, Diamond)
-- A method display_card: 
    Ex. "4 of Diamonds"
the list of players. 
List of strings: 

Add methods to distribute the cards and display the players' cards.
"""


class Card:
    def __init__(self, value, suit):
        if value < 1 or value > 13:
            raise ValueError("The card must have a value between 1 and 13")
        self.value = value
        self.suit = suit

    def display_card(self):
        print(f"{self.value} of {self.suit}")


class CardGame:
    """
    A deck of cards always contains 52 cards
    1 to 2 of each suit
    """

    def __init__(self, players_list):
        self.card_list = [Card(1, 'Spade'), Card(2, 'Spade'), Card(1, 'Heart'), Card(2, 'Heart'),
                          Card(1, 'Club'), Card(2, 'Club'), Card(1, 'Diamond'), Card(2, 'Diamond')]
        self.players_list = players_list

    def distribute_cards(self):
        """
        Return a dictionary
        {
        {Player1: [Card(1, 'Spade'), Card(2, 'Spade')]},
        {Player2: [Card(1, 'Heart'), Card(2, 'Heart')]},
        {Player3: [Card(1, 'Club'), Card(2, 'Club')]},
        {Player4: [Card(1, 'Diamond'), Card(2, 'Diamond')]}
        }
        """
        dictionary = {}
        cards_per_player = int(len(self.card_list) / len(self.players_list))
        distributed_cards = 0
        for player in self.players_list:
            dictionary[player] = self.card_list[distributed_cards:distributed_cards + cards_per_player]
            distributed_cards += cards_per_player
        return dictionary

    def display_players_cards(self):
        distribution = self.distribute_cards()
        for player, cards in distribution.items():
            print(f"Player: {player}")
            print("Cards:")
            for card in cards:
                card.display_card()


players_list = ['Player1', 'Player2', 'Player3', 'Player4']
card_game = CardGame(players_list)
card_game.display_players_cards()
