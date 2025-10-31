# Make a list of 5 student names. Then, add one new name to the list using .append() and remove one existing name using .remove().

if __name__ == "__main__":
    student_names = ["Kashif", "Khizar", "Umair", "Mehmood", "Qasim"]

    print(student_names)  # Output the initial list of student names

    # Add a new name
    student_names.append("Ubaid")

    print(student_names)  # Output the list after adding a new name

    # Remove an existing name
    student_names.remove("Khizar")

    print(student_names)  # Output the final list of student names

