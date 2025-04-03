import math

# Configuration for the robot application
# Parameters: robot name and time in minutes to clean one square meter
parameters = ("Wall-E", 1)  # Tuple containing robot details
robot_name = parameters[0]  # Name of the robot
time_per_m2 = parameters[1]  # Cleaning time per square meter (in minutes)

# Define zones to be cleaned using dictionaries
# Each dictionary contains the label, length (in meters), and width (in meters) of a zone
print("-- AREA OF THE ZONES --")
zone1 = {"label": "Zone 1", "length": 5, "width": 1.5}
zone2 = {"label": "Zone 2", "length": 3.09, "width": 4.8}
zone3 = {"label": "Zone 3", "length": 1.01, "width": 4.8}
zone4 = {"label": "Zone 4", "length": 0.9, "width": 2.2}

# Store all zones in a list for easy iteration
zones = [zone1, zone2, zone3, zone4]


def calculateTotalArea(zone_list):
    """
    Calculate the total cleaning area by summing the area of each zone.

    Args:
        zone_list (list): List of dictionaries representing the zones.

    Returns:
        float: Total area (in square meters), rounded to two decimal places.
    """
    total_area = 0
    for zone in zone_list:
        label = zone.get("label")  # Get the zone label
        length = zone.get("length")  # Get the length of the zone
        width = zone.get("width")  # Get the width of the zone
        area = round(length * width, 2)  # Calculate the area and round to 2 decimal places
        print(f"{label}: {length} m x {width} m = {area} m2")
        total_area += area  # Add to the total area
    return round(total_area, 2)


def cleaningTimeInMinutes(area_to_clean, time_per_square_meter):
    """
    Calculate the total cleaning time in minutes.

    Args:
        area_to_clean (float): Total area to be cleaned (in square meters).
        time_per_square_meter (int): Time (in minutes) required to clean one square meter.

    Returns:
        int: Total cleaning time (in minutes).
    """
    return round(area_to_clean * time_per_square_meter)


def timeInHours(minutes):
    """
    Convert cleaning time from minutes to a readable format in hours and minutes.

    Args:
        minutes (int): Total cleaning time (in minutes).

    Returns:
        str: Readable string indicating cleaning time in hours and minutes.
    """
    hours = math.floor(minutes / 60)  # Calculate full hours
    remaining_minutes = minutes % 60  # Calculate remaining minutes
    if minutes > 60:
        print(f"{robot_name}: This is going to take a while...")  # Provide feedback for long cleaning times
    if hours:
        if remaining_minutes:
            return f"{robot_name}: {hours} hours and {remaining_minutes} minutes will be required to complete the cleaning"
        else:
            return f"{robot_name}: {hours} hours will be required to complete the cleaning"
    else:
        return f"{robot_name}: {remaining_minutes} minutes will be required to complete the cleaning"


# Calculate the total cleaning area
area = calculateTotalArea(zones)
print("\n-- TOTAL AREA --")
print(f"The total area to be cleaned is {area} m2")

# Estimate the required cleaning time
required_time = cleaningTimeInMinutes(area, time_per_m2)
print("\n-- ESTIMATED TIME --")
print(timeInHours(required_time))
