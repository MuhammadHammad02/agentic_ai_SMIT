''' Start with the following dictionary:

car = {"brand": "Toyota", "year": 2020}
Add a new key color with a value (e.g., "Red"). Update the year to 2022. Print the updated dictionary.'''

if __name__ == "__main__":
    car = {"brand": "Toyota", "year": 2020
           }
    
    print("Original dictionary:")
    print(car)

    # Add a new key 'color' with value 'Red'
    car["color"] = "Red"

    # Update the year to 2022
    car["year"] = 2022

    # Print the updated dictionary
    print("Updated dictionary:")
    print(car)
