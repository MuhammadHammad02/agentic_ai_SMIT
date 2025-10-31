# Create a set {2, 4, 6}. Add the number 8 to the set, then remove the number 4. Print the updated set.

if __name__ == "__main__":
    my_set = {2, 4, 6}

    # Add the number 8 to the set
    my_set.add(8)

    # Remove the number 4 from the set
    my_set.remove(4)

    # Print the updated set
    print("Updated set:")
    print(my_set)