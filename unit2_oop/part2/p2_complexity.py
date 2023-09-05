# Unit 2; Part 2: Measuring Complexity
# Description: This file demonstrates how to measure the complexity of an algorithm.

# -------------------------------
# Time Complexity: Big O Notation
# Big O notation is used to describe the time complexity of an algorithm. It is a measure of how the runtime of an
#   algorithm scales with respect to the size of the input. For example, if an algorithm takes 1 second to run on an
#   input of size 10, and 2 seconds to run on an input of size 20, then the algorithm is said to have a linear time
#   complexity, or O(n) time complexity, where n is the size of the input.

# -------------------------------
# Section 0: A Linear Time Algorithm
# Description: This section demonstrates a linear time algorithm.

# This function takes in a list of integers and returns the sum of all the integers in the list. We will use the timeit
#   module to measure the runtime of this function.
import timeit


def sum_list(the_list):
    # Initialize a variable to hold the sum.
    total = 0

    # Iterate through the list and add each element to the total.
    for i in range(len(the_list)):
        total += the_list[i]

    # Return the total.
    return total


# Create a list of integers.
my_list = [1, 2, 3, 4, 5]
result_0 = timeit.timeit('sum_list(my_list)', globals=globals(), number=1000)
print("sum_list(my_list) took {} seconds to run 1000 times.".format(result_0))
# Because the function is linear, the runtime should increase linearly with the size of the input. We can verify this by
#   running the function with different input sizes and measuring the runtime.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Now that we have a list of 10 integers, let's measure the runtime of the function. It should be roughly twice as long
#   to run as the previous function call.
result_1 = timeit.timeit('sum_list(my_list)', globals=globals(), number=1000)
print("sum_list(my_list) took {} seconds to run 1000 times.".format(result_1))


# -------------------------------
# Section 1: A Constant Time Algorithm
# Description: This section demonstrates a constant time algorithm. Constant time algorithms are algorithms that take
#   the same amount of time to run regardless of the size of the input.

def get_first_element(the_list):
    # Return the first element in the list.
    return the_list[0]


# To demonstrate, we're going to add a million elements to a list and then measure the runtime of the function.
my_list = [i for i in range(1000000)]  # We will talk about comprehensions in a later unit.
for i in range(1, 10):
    result = timeit.timeit('get_first_element(my_list)', globals=globals(), number=1000)
    print("Run [{}]: get_first_element(my_list) took {} seconds to run 1000 times.".format(i, result))
    # Add another million elements to the list after each run.
    my_list += [i for i in range(1000000)]


# No matter how many elements we add to the list, the runtime of the function remains roughly the same. This is because
#   the function only ever accesses the first element in the list, which is always at the same memory address.
#   This is an example of a constant time algorithm.

# -------------------------------
# Section 2: A Quadratic Time Algorithm
# Description: This section demonstrates a quadratic time algorithm. Quadratic time algorithms are algorithms that take
#   the square of the size of the input to run.

def get_all_pairs(the_list):
    # Initialize a list to hold the pairs.
    pairs = []

    # Iterate through the list and add each pair to the list.
    for i in range(len(the_list)):
        for j in range(len(the_list)):
            pairs.append((the_list[i], the_list[j]))

    # Return the list of pairs.
    return pairs


my_list = [1, 2, 3, 4, 5]
result_0 = timeit.timeit('get_all_pairs(my_list)', globals=globals(), number=1000)
print("get_all_pairs(my_list) took {} seconds to run 1000 times.".format(result_0))

# Let's measure the runtime of the function with a list of ten items. It should be roughly 4 times as
#   long to run as the previous function call.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_1 = timeit.timeit('get_all_pairs(my_list)', globals=globals(), number=1000)
print("get_all_pairs(my_list) took {} seconds to run 1000 times.".format(result_1))

# Let's measure the runtime of the function with a list of twenty items. It should be roughly 16 times as
#   long to run as the previous function call.
my_list = [i for i in range(20)]
result_2 = timeit.timeit('get_all_pairs(my_list)', globals=globals(), number=1000)
print("get_all_pairs(my_list) took {} seconds to run 1000 times.".format(result_2))

# Other complexities include logarithmic time (O(log n)), exponential time (O(2^n)), and factorial time (O(n!)).
# We may discuss these in a later unit.

# TODO: Exercises?
