#  Make a list of 5 grocery items. Replace one item (e.g., change 'milk' to 'butter'). Print the updated list and the total number of items in the list.
if __name__ == "__main__":
    shopping_list = ["milk", "bread", "eggs", "cheese", "apples"]

    print(shopping_list)  # Output the initial shopping list

    # Replace 'milk' with 'butter'
    index = shopping_list.index("milk")
    shopping_list[index] = "butter"

    print(shopping_list)  # Output the updated shopping list

    # Print the total number of items in the list
    total_items = len(shopping_list)
    print(f"Total number of items in the shopping list: {total_items}")
    