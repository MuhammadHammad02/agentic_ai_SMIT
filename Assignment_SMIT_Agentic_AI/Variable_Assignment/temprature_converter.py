# Objective: Use expressions. Task: Convert Celsius to Fahrenheit using the formula: (celsius * 9/5) + 32.
if __name__ == "__main__":

    celsius = 25  # You can change this value to test with different temperatures

    fahrenheit = (celsius * 9/5) + 32

    print(f"{str(celsius)} degrees Celsius is equal to {str(fahrenheit)} degrees Fahrenheit.")
    print("{} degrees Celsius is equal to {} degrees Fahrenheit.".format(str(celsius), str(fahrenheit)))
    print(str(celsius) + " degrees Celsius is equal to " + str(fahrenheit) + " degrees Fahrenheit.")
