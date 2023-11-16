# Unit 1; Part 1: Variables in Python
# Description: This file demonstrates how to use variables in Python.

# Python is a dynamically typed language, which means that you do not need to
#   specify the type of variable when you declare it. The type of the variable
#   is inferred from the value that you assign to it.
my_string = "Hello World!"              # In Java, this would be `String my_string = "Hello World!"`
my_int = 5                              # In Java, this would be `int my_int = 5`
my_float = 5.0                          # In Java, this would be `float my_float = 5.0`
my_bool = True                          # In Java, this would be `boolean my_bool = true`
my_list = [1, 2, 3]                     # In Java, this would be `List<Integer> my_list = Arrays.asList(1, 2, 3)`
my_tuple = (1, 2, 3)                    # In Java, this would be `List<Integer> my_tuple = Arrays.asList(1, 2, 3)`
my_dict = {"a": 1, "b": 2, "c": 3}      # In Java, this would be `Map<String, Integer> my_dict = ...`

# You can also declare multiple variables on a single line.
a, b, c = 1, 2, 3

# Python also allows assignment the same value to multiple variables on a single line.
d = e = f = 1

# For fine-tuned control over Python's Garbage Collector, you can use the del keyword to delete a variable.
id(d)   # Get the memory address of d
#del d   # Delete the variable d

# If you need to know the type, use the type() function to get the type of variable Python inferred.
type(my_string)
type(my_int)
type(my_float)
type(my_bool)
type(my_list)
type(my_tuple)
type(my_dict)

print(id(d))


# Exercise 1: Create a variable called `my_name` and assign it your name.
my_name = "travis"
print(my_name)
# Exercise 2: Create a variable called `my_age` and assign it your age.
print (3*(2**3))
print (2//3)
print (2.0//3.0)

