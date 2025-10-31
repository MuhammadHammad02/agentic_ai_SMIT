#  Given a list [1, 2, 2, 3, 4, 4, 5]. Convert this list to a set to automatically remove duplicates. Print both the original list and the resulting set.

if __name__ == "__main__":
    original_list = [1, 2, 2, 3, 4, 4, 5]
    converted_set = set(original_list)

    print("Original list:")
    print(original_list)

    print("\nConverted set (duplicates removed):")
    print(converted_set)

