# Unit 1; Part 3: Control Flow in Python
# Description: This file demonstrates how to use control flow in Python.

# --------------------------------------------------
# Section 0: If statements
# The if statement is used to check a condition. If the condition is true, then the code inside the
#   if statement is executed. Otherwise, the code inside the if statement is skipped.
if True:
    print("This will be printed")

if 1:
    print("Integers like '1' are converted to True")

if "true":
    print("String literals are also converted to True")

if 0:
    print("Integers like '0' are converted to False, this will not print.")

# In Java, we would have to do something like this:
#   if (true) {
#       System.out.println("Hello World!");
#   }

# Python is an indentation-sensitive language. This means that the indentation of the code matters.
#   The code inside the if statement is indented by 4 spaces. This is how Python knows that the code
#   is inside the if statement. The code inside the if statement is called a block of code. The block
#   of code ends when the indentation returns to the previous level. In this case, the block of code
#   ends when the indentation returns to the same level as the if statement.
if True:
    print("I'm in the code block")
print("I'm not in the code block")

# --------------------------------------------------
# Section 1: If-else statements
# The if-else statement is used to check a condition. If the condition is true, then the code inside
#   the if statement is executed. Otherwise, the code inside the else statement is executed.
if False:
    print("This will not be printed")
else:
    print("This will be printed")

# In Java, we would have to do something like this:
#   if (false) {
#       System.out.println("Hello World!");
#   } else {
#       System.out.println("Goodbye World!");
#   }

# --------------------------------------------------
# Section 2: If-elif-else statements
# The if-elif-else statement is used to check multiple conditions. If the first condition is true,
#   then the code inside the if statement is executed. Otherwise, the next condition is checked.
#   If the second condition is true, then the code inside the elif statement is executed. Otherwise,
#   the code inside the else statement is executed.
if False:
    print("I'm the first condition")
elif True:
    print("I'm the second condition")
else:
    print("I'm printed if none of the conditions are true")

# In Java, we would have to do something like this:
#   if (false) {
#       System.out.println("Hello World!");
#   } else if (true) {
#       System.out.println("Goodbye World!");
#   } else {
#       System.out.println("This will not be printed");
#   }

# --------------------------------------------------
# Section 3: For loops
# The for loop is used to iterate over a sequence of items. The sequence can be a list, tuple, string,
#   dictionary, or range. The for loop will iterate over each item in the sequence and execute the
#   code inside the for loop for each item.
for i in range(5):              # range(5) is a sequence of numbers from 0 to 4
    print(i)                    # Print the current number

for i in range(1, 5):           # range(1, 5) is a sequence of numbers from 1 to 4
    print(i)                    # Print the current number

for i in range(1, 5, 2):        # range(1, 5, 2) is a sequence of numbers from 1 to 4, incrementing by 2
    print(i)                    # Print the current number

for i in [1, 2, 3, 4]:          # [1, 2, 3, 4] is a list of numbers
    print(i)                    # Print the current number

for i in (1, 2, 3, 4):          # (1, 2, 3, 4) is a tuple of numbers
    print(i)                    # Print the current number

for i in "Hello World!":        # "Hello World!" is a string
    print(i)                    # Print the current character

for i in {"a": 1, "b": 2}:      # {"a": 1, "b": 2} is a dictionary
    print(i)                    # Print the current key


# In Java, we would have to do something like this:
#   for (int i = 0; i < 5; i++) {
#       System.out.println(i);
#   }

# --------------------------------------------------
# Section 4: While loops
# The while loop is used to execute a block of code while a condition is true.
i = 0
while i < 5:
    print(i)                   # Print the current number
    i += 1

# In Java, we would have to do something like this:
#   int i = 0;
#   while (i < 5) {
#       System.out.println(i);
#       i++;
#   }

# --------------------------------------------------
# Section 5: Break and continue
# The break statement is used to exit a loop. The continue statement is used to skip the rest of the
#   code in the current iteration of the loop.
for i in range(10):
    if i == 5:
        print("Exiting the loop")
        break                   # Exit the loop
    print(i)                    # Print the current number

for i in range(10):
    if i == 5:
        print("Skipping the rest of the code in this iteration")
        continue                # Skip the rest of the code in this iteration
    print(i)                    # Print the current number

# In Java, we would have to do something like this:
#   for (int i = 0; i < 10; i++) {
#       if (i == 5) {
#           System.out.println("Exiting the loop");
#           break;
#       }
#       System.out.println(i);
#   }
#
#   for (int i = 0; i < 10; i++) {
#       if (i == 5) {
#           System.out.println("Skipping the rest of the code in this iteration");
#           continue;
#       }
#       System.out.println(i);
#   }

# --------------------------------------------------
# Section 6: Try-except blocks
# The try-except block is used to catch exceptions. If an exception is raised in the try block, then
#   the code inside the except block is executed. Otherwise, the code inside the except block is
#   skipped.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# The try-except-else block is used to catch exceptions. If an exception is raised in the try block,
#   then the code inside the except block is executed. Otherwise, the code inside the else block is
#   executed.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exceptions were raised")

# Try-catch-finally blocks are used to catch exceptions. If an exception is raised in the try block,
#   then the code inside the catch block is executed. Otherwise, the code inside the finally block is
#   executed.
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This code will always be executed")

# We will cover exceptions in a later unit. For now, just know that 1 / 0 will raise a ZeroDivisionError.

# In Java, we would have to do something like this:
#   try {
#       System.out.println(1 / 0);
#   } catch (ArithmeticException e) {
#       System.out.println("Cannot divide by zero");
#   }

# --------------------------------------------------
# Section 7: Pass
# The pass statement is used as a placeholder for code that has not been implemented yet.
if True:
    pass                        # Do nothing

# In Java, we would have to do something like this:
#   if (true) {
#       // Do nothing
#   }

# --------------------------------------------------
# Section 8: String manipulation
# Strings can be manipulated using the following methods:
#   - str.lower() - Converts the string to lowercase
#   - str.upper() - Converts the string to uppercase
#   - str.title() - Converts the string to title case
#   - str.strip() - Removes leading and trailing whitespace
#   - str.lstrip() - Removes leading whitespace
#   - str.rstrip() - Removes trailing whitespace
#   - str.replace(old, new) - Replaces all occurrences of old with new
#   - str.split() - Splits the string into a list of strings
#   - str.join(list) - Joins the list of strings into a single string
# For more methods, see https://docs.python.org/3/library/stdtypes.html#string-methods
string_a = "this is a string"
string_b = "THIS IS A STRING"
string_c = "This Is A String"
print(string_a.upper())
print(string_b.lower())
print(string_a + string_b + string_c)
print(" ".join([string_a, string_b, string_c]))

# --------------------------------------------------
# Section 9: Arithmetic operators
# Python supports the following arithmetic operators:
#   - Addition: +
#   - Subtraction: -
#   - Multiplication: *
#   - Division: /
#   - Floor Division: //
#   - Modulus: %
#   - Exponentiation: **
#   - Negation: -
#   - Absolute Value: abs()
#   - Round: round()
# For more operators, see https://docs.python.org/3/library/operator.html
print(1 + 1)            # Addition
print(1 - 1)            # Subtraction
print(2 * 2)            # Multiplication
print(4 / 2)            # Division
print(5 // 2)           # Floor Division
print(5 % 2)            # Modulus
print(2 ** 3)           # Exponentiation
print(-1)               # Negation
print(abs(-1))          # Absolute Value
print(round(1.5))       # Round


# --------------------------------------------------
# Section 10: Comparison operators
# Python supports the following comparison operators:
#   - Equal: ==
#   - Not Equal: !=
#   - Greater Than: >
#   - Less Than: <
#   - Greater Than or Equal To: >=
#   - Less Than or Equal To: <=
# For more operators, see https://docs.python.org/3/library/operator.html
print(1 == 1)           # Equal
print(1 != 1)           # Not Equal
print(1 > 1)            # Greater Than
print(1 < 1)            # Less Than
print(1 >= 1)           # Greater Than or Equal To
print(1 <= 1)           # Less Than or Equal To

# --------------------------------------------------
# Section 11: Logical operators
# Python supports the following logical operators:
#   - And: and
#   - Or: or
#   - Not: not
# For more operators, see https://docs.python.org/3/library/operator.html
print(True and True)    # And
print(True or True)     # Or
print(not True)         # Not

# --------------------------------------------------
# Section 12: Bitwise operators
# Python supports the following bitwise operators:
#   - And: &
#   - Or: |
#   - Xor: ^
#   - Not: ~
#   - Left Shift: <<
#   - Right Shift: >>
# For more operators, see https://docs.python.org/3/library/operator.html
print(0b101 & 0b110)    # And
print(0b101 | 0b110)    # Or
print(0b101 ^ 0b110)    # Xor
print(~0b101)           # Not
print(0b101 << 2)       # Left Shift
print(0b101 >> 2)       # Right Shift

# --------------------------------------------------
# Section 13: Casting
# Python supports the following casting functions:
#   - int() - Converts the value to an integer
#   - float() - Converts the value to a float
#   - str() - Converts the value to a string
#   - bool() - Converts the value to a boolean
# For more functions, see https://docs.python.org/3/library/functions.html
print(int(1.5))         # Convert to an integer
print(float(1))         # Convert to a float
print(str(1))           # Convert to a string
print(bool(1))          # Convert to a boolean

# --------------------------------------------------
the_list = ['a', 'b', 'c', 1, 2, 3]
# Exercise 1: Iterate the above list and add each item to a string named 'exercise_one'.
# Exercise 2: Iterate the above list and add each item to a string named 'exercise_two',
#   but stop the loop if the item is an integer.
# Exercise 3: Create a loop that adds the numbers 1 to 10 to a string named 'exercise_three',
#   but skips the number 5 and stops after printing 8.
exercise_one = ""
exercise_two = ""
exercise_three = ""
