# Unit 3; Part 2: IO in Python
# Description: This file demonstrates how to use file IO in Python.

# --------------------------------------------------
# Section 0: Reading from a file
# The open() function opens a file and returns a file object. This is how we read from a file.
# The first argument is the path to the file. The second argument is the mode in which we want to open the file.
#   The default mode is "r", which stands for "read". Other modes include "w" for "write" and "a" for "append".
with open('res/example.txt', 'r') as file:
    contents = file.read()                              # Read the entire file into a string.
    print(contents)                                     # Print the contents of the file.

# In Java, we would have to do something like this:
#   BufferedReader br = new BufferedReader(new FileReader("res/example.txt"));
#   String line;
#   while ((line = br.readLine()) != null) {
#       System.out.println(line);
#   }
#   br.close();

# Python can also read the file line by line.
with open('res/example.txt', 'r') as file:
    for line in file:
        print(line)

# Additionally, you can open two files at the same time.
with open('res/example.json', 'r') as jsonFile, open('res/example.yaml', 'r') as yamlFile:
    jsonString = jsonFile.read()
    yamlString = yamlFile.read()
    print(jsonString)
    print(yamlString)

# --------------------------------------------------
# Section 2: Writing to a file
# The open() function opens a file and returns a file object. This is also how we write to a file.
with open('res/example_write.txt', 'w') as file:
    file.write("Hello World!")                          # Write "Hello World!" to the file.

# In Java, we would have to do something like this:
#   BufferedWriter bw = new BufferedWriter(new FileWriter("res/example.txt"));
#   bw.write("Hello World!");
#   bw.close();

# --------------------------------------------------
# Section 3: Appending to a file
# Using the "a" mode, we can append to a file.
with open('res/example_write.txt', 'a') as file:
    appending_data = "I'm appending to the file!\n"     # Create a string to append to the file.
    file.write(appending_data)                          # Append "Hello World!" to the file.

# --------------------------------------------------
# Section 4: Using user input to write to a file
# The input() function is used to get user input from the console.
user_input = input("Enter something: ")
with open('res/example_write.txt', 'a') as file:
    file.write(f'{user_input}\n')                       # Append the user's input to the file.

with open('res/example_write.txt', 'r') as file:
    contents = file.read()                              # Read the entire file into a string.
    print(contents)                                     # Print the contents of the file.

# --------------------------------------------------
# Section 5: Creating a file
# The open() function can also be used to create a file!
with open('res/example_create.txt', 'w') as file:
    file.write("Hello World!")                          # Write "Hello World!" to the file.

# --------------------------------------------------
# Exercise 1: Create a file called `my_file.txt` and write you name to it in this format:
#   Hello, my name is {name}. I am {age} years old.
#   My favorite color is {color}.
