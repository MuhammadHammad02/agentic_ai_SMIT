# Make a list of numbers [5, 10, 15, 20]. Print:

from statistics import mean


if __name__ == "__main__":
    numbers = [5, 10, 15, 20]

   # The total sum of the numbers using sum()
    total_sum = sum(numbers)
    print("Total Sum of Numbers:")
    print(total_sum)

    # The average of the numbers
    average = total_sum / len(numbers)
    print("\nAverage of Numbers:")
    print(average)

    average_alternate = mean(numbers)
    print("\nAverage of Numbers (Alternate Method):")
    print(average_alternate)