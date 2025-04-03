import time

NB_ELEVATORS = 4  # Number of elevators in the network
NB_FLOORS = 3  # Number of floors in the building
MAX_CAPACITY = 12000  # Maximum weight capacity in pounds (lbs)
IS_PARKING = True  # Indicates if the building has a parking floor


class Person:
    """
    Represents a person using the elevator.
    Attributes:
        name (str): The name of the person.
        weight (int): The weight of the person in pounds.
    """

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name


class Elevator:
    """
    Represents an elevator in the simulation.
    Attributes:
        unique_id (any): A unique identifier for the elevator.
        floor (int): The current floor of the elevator.
        capacity (int): Maximum weight capacity of the elevator in pounds.
        emergency (bool): Whether the elevator is in emergency mode.
        passengers (list): List of passengers currently in the elevator.
    """

    def __init__(self, unique_id, floor=0, capacity=MAX_CAPACITY, emergency=False):
        self.unique_id = unique_id
        self.floor = floor
        self.capacity = capacity
        self.emergency = emergency
        self.passengers = []

    def __str__(self):
        """
        Returns a string representation of the elevator's state.
        """
        return (f"ID: {self.unique_id} | "
                f"Floor: {self.floor} | "
                f"Capacity (lbs): {self.capacity:,} | "
                f"Passengers: {[str(p) for p in self.passengers]} | "
                f"Weight: {sum(p.weight for p in self.passengers)} | "
                f"Emergency: {'Yes' if self.emergency else 'No'}")

    def is_overweight(self):
        """
        Checks if the elevator is over its maximum weight capacity.
        Returns:
            bool: True if overweight, False otherwise.
        """
        total_weight = sum(p.weight for p in self.passengers)
        return total_weight > self.capacity

    def add_passenger(self, person):
        """
        Adds a passenger to the elevator.
        Args:
            person (Person): The person to add to the elevator.
        """
        self.passengers.append(person)
        print(f"{person.name} entered the elevator.")

    def remove_passenger(self, person_name):
        """
        Removes a passenger from the elevator by name.
        Args:
            person_name (str): The name of the passenger to remove.
        """
        if person_name in [p.name for p in self.passengers]:
            self.passengers = [p for p in self.passengers if p.name != person_name]
            print(f"{person_name} has exited the elevator.")
        else:
            print(f"{person_name} is not in the elevator.")

    def move_to_floor(self, target_floor):
        """
        Moves the elevator to the specified floor if it's within bounds and not overweight.
        Args:
            target_floor (int): The floor to move the elevator to.
        """
        if not self.is_overweight():
            if 0 <= target_floor < NB_FLOORS and self.floor != target_floor:
                print(f"Elevator {self.unique_id} is moving from floor {self.floor} to floor {target_floor}.")
                time.sleep(1)  # Simulates the time taken to move between floors
                self.floor = target_floor
                print(f"Elevator {self.unique_id} is now on floor {self.floor}.")
            else:
                print(f"Floor {target_floor} is invalid. Please choose a floor between 0 and {NB_FLOORS - 1}.")
        else:
            print(f"Overcapacity! Elevator {self.unique_id} cannot proceed.")


def main():
    """
    Main function to run the elevator simulation.
    Creates passengers, initializes an elevator, and simulates its operation.
    """
    # Creating some people with their weights in pounds
    alice = Person("Alice", 130)
    bob = Person("Bob", 180)
    sam = Person("Sam", 175)

    # Initializing the elevator with a capacity of 12,000 lbs
    elevator = Elevator("A", floor=0, capacity=MAX_CAPACITY)

    # Adding people to the elevator
    elevator.add_passenger(alice)
    elevator.add_passenger(bob)
    elevator.add_passenger(sam)

    # Moving the elevator
    elevator.move_to_floor(2)

    # Displaying the elevator's state
    print(elevator)

    # Removing passengers from the elevator
    elevator.remove_passenger("Alice")
    elevator.remove_passenger("Sam")
    print(elevator)

    # Moving the elevator back to the ground floor
    elevator.move_to_floor(0)


if __name__ == "__main__":
    main()
