''' Create a dictionary named student with the following information:

student = {
  "name": "Ali",
  "age": 20,
  "grade": "A"
}
Print a sentence using this dictionary: Ali is 20 years old and got grade A.'''

if __name__ == "__main__":
    student = {
        "name": "Ali",
        "age": 20,
        "grade": "A"
    }

    print(f"{student['name']} is {student['age']} years old and got grade {student['grade']}.")
    