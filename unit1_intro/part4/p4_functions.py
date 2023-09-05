# Unit 1; Part 4: Functions in Python
# Description: This file demonstrates how to use functions in Python.

# --------------------------------------------------
# Section 0: Defining and calling functions
# Functions are defined using the def keyword.
def my_function():
    print("Hello World!")


# Functions are called using the function name and parentheses.
my_function()


# In Java, we would have to do something like this:
#   public static void myFunction() {
#       System.out.println("Hello World!");
#   }
#   myFunction();

# --------------------------------------------------
# Section 1: Function parameters
# Functions can take parameters.
def my_function_with_parameters(name, age):
    print("Hello, my name is {} and I am {} years old.".format(name, age))


# Functions are called using the function name and parentheses.
my_function_with_parameters("John Doe", 20)


# In Java, we would have to do something like this:
#   public static void myFunctionWithParameters(String name, int age) {
#       System.out.println("Hello, my name is " + name + " and I am " + age + " years old.");
#   }
#   myFunctionWithParameters("John Doe", 20);

# --------------------------------------------------
# Section 2: Function return values
# Functions can return values.
def my_function_with_return_value(name, age):
    return "Hello, my name is {} and I am {} years old.".format(name, age)


# Functions are called using the function name and parentheses.
print(my_function_with_return_value("John Doe", 20))


# In Java, we would have to do something like this:
#   public static String myFunctionWithReturnValue(String name, int age) {
#       return "Hello, my name is " + name + " and I am " + age + " years old.";
#   }
#   System.out.println(myFunctionWithReturnValue("John Doe", 20));

# --------------------------------------------------
# Section 3: Function default parameters
# Functions can have default parameters.
def my_function_with_default_parameters(name, age=20):
    print("Hello, my name is {} and I am {} years old.".format(name, age))


def my_function_with_default_parameters_and_return(name="John Doe", age=20):
    return "Hello, my name is {} and I am {} years old.".format(name, age)


# Functions are called using the function name and parentheses.
my_function_with_default_parameters("John Doe", 20)
my_function_with_default_parameters("John Doe")  # age defaults to 20


# --------------------------------------------------
# Section 4: Function type annotations Functions can have type annotations. This is not required,
#   but it is good practice, as it makes your code more readable.
def my_function_with_type_annotations(name: str, age: int) -> str:
    """
    This function takes a name and an age and returns a string. This is the docstring. It is used to describe the
    function. It is good practice to include a docstring for every function you write.
    :param name:    The name of the person.
    :param age:     The age of the person.
    :return:        A string containing the name and age of the person.
    """
    return "Hello, my name is {} and I am {} years old.".format(name, age)


# --------------------------------------------------
# Section 5: Function keyword arguments
# Functions can take keyword arguments.
def my_function_with_keyword_arguments(**keyword_arguments) -> None:
    """
    This function takes keyword arguments and prints them.
    :param keyword_arguments:   The keyword arguments.
    :return:                    None
    """
    print(keyword_arguments)


# Functions are called using the function name and parentheses.
my_function_with_keyword_arguments(name="John Doe", age=20)

# The '**' operator is used to unpack a dictionary. This dictionary can be evaluated at runtime.
my_function_with_keyword_arguments(**{"name": "John Doe", "age": 20})


# In Java, we would have to do something like this:
#   public static void myFunctionWithKeywordArguments(Map<String, Object> keywordArguments) {
#       System.out.println(keywordArguments);
#   }


# --------------------------------------------------
# Section 6: Function variable arguments
# Functions can take variable arguments.
def my_function_with_variable_arguments(*variable_arguments) -> None:
    """
    This function takes variable arguments and prints them.
    :param variable_arguments:
    :return:
    """
    print(variable_arguments)


# The '*' operator is used to unpack a list. This list can be evaluated at runtime.
my_function_with_variable_arguments(*["John Doe", 20])


# In Java, we would have to do something like this:
#   public static void myFunctionWithVariableArguments(List<Object> variableArguments) {
#       System.out.println(variableArguments);
#   }


# --------------------------------------------------
# Section 7: Function scope
# Functions have their own scope. Variables defined inside a function are not accessible outside of the function.
def my_function_with_scope() -> None:
    """
    This function demonstrates function scope.
    :return:   None
    """
    my_variable = "Hello World!"  # This variable is only accessible inside this function.
    print(my_variable)


# Calling my_variable here would result in an error.

# --------------------------------------------------
# Section 8: Function recursion
# Functions can call themselves. This is called recursion.
def my_function_with_recursion(n) -> None:
    """
    This function demonstrates recursion.
    :param n:   The number to start counting down from.
    :return:    None
    """
    if n > 0:
        print(n)
        my_function_with_recursion(n - 1)


# --------------------------------------------------
# Section 9: Functions within functions
# Functions can be defined within other functions. These functions are called inner functions. Inner functions are
#   only accessible within the outer function.
def my_function_with_inner_function() -> None:
    """
    This function demonstrates inner functions.
    :return:    None
    """

    def my_inner_function():
        print("Hello World!")

    my_inner_function()

# Calling my_inner_function here would result in an error.

# Exercise 1: Create a function called `exercise_1` that takes 3 arguments, one integer, one string and a list.
#   Annotate the function with the correct types. The function should return a string that contains all the arguments.
# Exercise 2: Create a function called `exercise_2` that recursively prints the first 10 multiples of the first argument.
#  Annotate the function with the correct types. The function should return the last multiple.
# Exercise 3: Create a function called `exercise_3` that builds a string from keyword arguments. Annotate the function.
#   The function should return a string.



# Uncomment the following lines to test your code after you have completed the exercises.
# exercise_1(1, "string", [1, 2, 3])
# exercise_2(2)
# exercise_3(name="John Doe", age=20)