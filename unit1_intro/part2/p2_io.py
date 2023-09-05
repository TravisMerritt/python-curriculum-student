# Unit 1; Part 2: IO in Python
# Description: This file demonstrates how to use file IO in Python.

# Section 0: Outputting to console
# The print() function is used to output to the console.
print("Hello World!")

# You can also print multiple things on the same line.
print("Hello", "World!")

# To print a formatted string of variables, use the format() function.
print("Hello, my name is {} and I am {} years old.".format("John Doe", 20))
# The shorthand for this is:
name = "John Doe"
age = 20
print(f"Hello, my name is {name} and I am {age} years old.")

# --------------------------------------------------
# Section 1: Reading from a file
# The open() function opens a file and returns a file object. This is how we read from a file.
# The first argument is the path to the file. The second argument is the mode in which we want to open the file.
#   The default mode is "r", which stands for "read". Other modes include "w" for "write" and "a" for "append".
with open('example.txt', 'r') as file:
    contents = file.read()                              # Read the entire file into a string.
    print(contents)                                     # Print the contents of the file.

# In Java, we would have to do something like this:
#   BufferedReader br = new BufferedReader(new FileReader("example.txt"));
#   String line;
#   while ((line = br.readLine()) != null) {
#       System.out.println(line);
#   }
#   br.close();

# Python can also read the file line by line.
with open('example.txt', 'r') as file:
    for line in file:
        print(line)

# You can also open two files at the same time.
with open('example.json', 'r') as jsonFile, open('example.yaml', 'r') as yamlFile:
    jsonString = jsonFile.read()
    yamlString = yamlFile.read()
    print(jsonString)
    print(yamlString)

# --------------------------------------------------
# Section 2: Writing to a file
# The open() function opens a file and returns a file object. This is also how we write to a file.
with open('example_write.txt', 'w') as file:
    file.write("Hello World!")                          # Write "Hello World!" to the file.

# In Java, we would have to do something like this:
#   BufferedWriter bw = new BufferedWriter(new FileWriter("example.txt"));
#   bw.write("Hello World!");
#   bw.close();

# --------------------------------------------------
# Section 3: Appending to a file
# Using the "a" mode, we can append to a file.
with open('example_write.txt', 'a') as file:
    appending_data = "I'm appending to the file!\n"     # Create a string to append to the file.
    file.write(appending_data)                          # Append "Hello World!" to the file.

# --------------------------------------------------
# Section 4: Using user input to write to a file
# The input() function is used to get user input from the console.
user_input = input("Enter something: ")
with open('example_write.txt', 'a') as file:
    file.write(f'{user_input}\n')                       # Append the user's input to the file.

with open('example_write.txt', 'r') as file:
    contents = file.read()                              # Read the entire file into a string.
    print(contents)                                     # Print the contents of the file.

# --------------------------------------------------
# Section 5: Creating a file
# The open() function can also be used to create a file!
with open('example_create.txt', 'w') as file:
    file.write("Hello World!")                          # Write "Hello World!" to the file.

# --------------------------------------------------
# Exercise 1: Create a file called `my_file.txt` and write you name to it in this format:
#   Hello, my name is {name}. I am {age} years old.
#   My favorite color is {color}.
with open('my_file.txt', 'w') as my_file:
    my_file.write("Hello, my name is {}. I am {} years old.\nMy favorite color is {}".format("John Doe", 20, 'green'))
