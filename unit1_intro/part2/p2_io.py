# Unit 3; Part 2: IO in Python
# Description: This file demonstrates how to use system IO in Python.

# --------------------------------------------------
# Section 0: Outputting to console
# The print() function is used to output to the console. It's useful for debugging and for displaying information to
#   the user. The print() function can take any number of arguments, and will print them all on the same line.
print("Hello World!")
print("Hello", "World!")

# To print a formatted string of variables, use the format() function.
print("Hello, my name is {} and I am {} years old.".format("John Doe", 20))

# The shorthand for this is:
name = "John Doe"
age = 20
# The 'f' before the string tells Python to format the string.
print(f"Hello, my name is {name} and I am {age} years old.")

# In Java, we would have to do something like this:
#   System.out.println("Hello World!");
#   System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");

# --------------------------------------------------
# Section 1: Reading input from the user
# The input() function is used to get user input from the console. It takes a single argument, which is the prompt to
#   display to the user.
user_input = input("Enter something: ")
print(f"You entered: {user_input}")

# In Java, we would have to do something like this:
#   Scanner scanner = new Scanner(System.in);
#   System.out.print("Enter something: ");
#   String userInput = scanner.nextLine();
#   System.out.println("You entered: " + userInput);

# --------------------------------------------------
# Exercise 1: Write a program that asks the user for their name and birth year, then calculates their age.

