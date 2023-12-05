import random

# List of 15 Students
names = ["1", "2", "#3", "#4", "#5","6", "#7","8","#9", "#10", "#11", "#12"]



def select_next_member():
    if names:
        # Randomly select a name and remove it from the list
        name = random.choice(names)
        names.remove(name)
        return name
    else:
        return "All members have been selected."

while True:
    number_students = input("How many students are in the class?")
    names = list(range(1,int(number_students)+1))

    test =  {"name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis","name":"Travis"}
    print (names)

    user_input = input("Would you like to select a group memner? (yes/no) ")
    if user_input.lower() == 'yes':
        print("Your next member will be: ", select_next_member())
    elif user_input.lower() == 'no':
        print("Thank you for playing Select that Presenter.")
        break
    else:
        print("Invalid input. Please enter Yes or No.")