# Create a tuple with repeating colors: ('red', 'blue', 'red', 'green', 'red'). Print how many times "red" appears in the tuple and find its first index.
if __name__ == "__main__":
    colors = ('red', 'blue', 'red', 'green', 'red')
    
    # Count how many times "red" appears
    red_count = colors.count('red')
    print(f"'red' appears {red_count} times in the tuple.")
    
    # Find the first index of "red"
    first_red_index = colors.index('red')
    print(f"The first index of 'red' is {first_red_index}.")

    
