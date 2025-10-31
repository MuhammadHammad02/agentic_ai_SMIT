#  Create a dictionary of 3 countries with their capitals (e.g., Pakistan: Islamabad, Turkey: Ankara, Japan: Tokyo). Loop through the dictionary and print each country and its capital in the format: Country → Capital.
if __name__ == "__main__":
    countries_capitals = {
        "Pakistan": "Islamabad",
        "Turkey": "Ankara",
        "Japan": "Tokyo"
    }

    for country, capital in countries_capitals.items():
        print(f"{country} : {capital}")

