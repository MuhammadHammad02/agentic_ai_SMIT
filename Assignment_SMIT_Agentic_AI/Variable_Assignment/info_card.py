#Objective: Combine string and numeric variables. Task: Store your name, age, and favorite hobby in variables and print:

if __name__ == "__main__":
    
    name = "Muhammad Hammad"
    age = 36
    hobby = "Coding"

    print("My name is " + name + ", I am " + str(age) + " years old and my favorite hobby is " + hobby + ".")
    print(f"My name is {name}, I am {str(age)} years old and my favorite hobby is {hobby}.")
    print("My name is {}, I am {} years old and my favorite hobby is {}.".format(name, str(age), hobby))