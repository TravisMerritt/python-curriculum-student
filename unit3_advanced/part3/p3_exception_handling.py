# Unit 3; Part 3: Exception Handling in Python
# Description: This file demonstrates how to use exception handling in Python.

# --------------------------------------------------
# Section 0: Try/Except
# The try/except block is used to catch exceptions. Exceptions are errors that occur during runtime.
# The try block contains code that may throw an exception and the except block contains code that
# handles the exception.
try:
    # This code will throw an exception.
    print(1 / 0)
except:
    # This code will handle the exception.
    print("An error occurred!")

# In Java, we would have to do something like this:
#   try {
#       System.out.println(1 / 0);
#   } catch (Exception e) {
#       System.out.println("An error occurred!");
#   }

# --------------------------------------------------
# Section 1: Try/Except with specific exception
# The try/except block can also catch specific exceptions, similar to Java's try/catch block.
try:
    # This code will throw an exception.
    print(1 / 0)
except ZeroDivisionError:
    # This code will handle the exception.
    print("An error occurred!")

# In Java, we would have to do something like this:
#   try {
#       System.out.println(1 / 0);
#   } catch (ArithmeticException e) {
#       System.out.println("An error occurred!");
#   }

# --------------------------------------------------
# Section 2: Try/Except with multiple specific exceptions
# The try/except block can also catch multiple specific exceptions, this is for useful for displaying
# different error messages depending on the caught exception.
try:
    # This code will throw an exception.
    print(1 / 0)
except ZeroDivisionError:
    # This code will handle the exception.
    print("An error occurred!")
except TypeError:
    # This code will handle the exception.
    print("Another error occurred!")

# In Java, we would have to do something like this:
#   try {
#       System.out.println(1 / 0);
#   } catch (ArithmeticException e) {
#       System.out.println("An error occurred!");
#   } catch (Exception e) {
#       System.out.println("Another error occurred!");
#   }

# --------------------------------------------------
# Section 3: Try/Except with generic exception
# The try/except block can also catch generic exceptions, this is useful for displaying a generic error
# but should be used sparingly. It's better to catch specific exceptions, as we can attempt to recover
# from the error or warn the user about the issue specifically without guessing.
try:
    # This code will throw an exception.
    print(1 / 0)
except Exception as e:
    # The keyword 'as' is used to assign the exception to a variable.
    # The variable can then be used to get more information about the exception.
    print(e)  # Get the traceback of the exception.

# --------------------------------------------------
# Section 4: Try/Except with finally
# The try/except block can also have a 'finally' block. The 'finally' block will always execute, regardless
# of whether an exception was thrown.
try:
    # This code will throw an exception.
    print(1 / 0)
except Exception as e:
    # This code will handle the exception.
    print(e)
finally:
    # This code will always execute.
    print("This code will always execute!")

# For more information on specific and common Python exceptions, refer to this documentation:
#   https://docs.python.org/3/library/exceptions.html

# --------------------------------------------------
# Section 5: Throw an exception
# The raise keyword is used to throw an exception. This is useful for creating custom exceptions.
try:
    # This code will throw an exception.
    raise Exception("This is a custom exception!")
except Exception as e:
    # This code will handle the exception.
    print(e)

# --------------------------------------------------
# Exercise 1: Write a program that takes in two positive numbers from the user and divides them. Handle any exceptions
#   that may occur. Some exceptions to consider are: ZeroDivisionError, ValueError, TypeError, etc.
# Exercise 2: Write a program that attempts to open a file. Add a check that verifies the file is found and handles if
#   it is not found. Some exceptions to consider are: FileNotFoundError, IOError, etc. Write to the file your:
#     - Name
#     - Favorite pizza topping
#     - Favorite movie
#     - Favorite song
#     - Favorite programming language
#   Then read the file and, throwing an error if the file contains numbers.
# Exercise 3: Write a program that creates a list of 1000 random numbers. Then prompt the user to select an index
#   between 0 and 999. Handle any exceptions that may occur. Some exceptions to consider are:
#   IndexError, ValueError, etc.

