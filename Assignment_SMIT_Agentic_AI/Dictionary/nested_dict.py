''' Create a dictionary named students with nested dictionaries for each student's information:

students = {
  "Ali": {"age": 18, "grade": "A"},
  "Sara": {"age": 19, "grade": "B"}
}
Loop through the students dictionary and print each student's name along with their grade.

'''
if __name__ == "__main__":
    students = {
  "Ali": {"age": 18, "grade": "A"},
  "Sara": {"age": 19, "grade": "B"}
}
    for student in students:
        print(f"The age of {student} is {students[student]['age']} and grade is {students[student]['grade']}.")
    