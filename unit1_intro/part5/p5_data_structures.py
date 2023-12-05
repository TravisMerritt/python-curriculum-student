# Unit 1; Part 5: Data Structures of Python
# Description: This file demonstrates how to use data structures in Python.

# --------------------------------------------------
# Section 0: Lists
# Lists are Python's version of arrays. They are mutable and can contain elements of different types.
my_list = [1, 2, 3, 4, 5]                   # In Java, this would be `List<Integer> my_list = Arrays.asList(1, 2, 3, 4, 5)`
# my_list.append(6)                         # In Java, this would be `my_list.add(6)`
# my_list.insert(0, 0)                      # In Java, this would be `my_list.add(0, 0)`
# my_list.remove(0)                         # In Java, this would be `my_list.remove(0)`
# my_list.pop()                             # In Java, this would be `my_list.remove(my_list.size() - 1)`
# my_list.pop(0)                            # In Java, this would be `my_list.remove(0)`
# my_list.clear()                           # In Java, this would be `my_list.clear()`

# Negative indices can be used to access elements from the end of the list.
# my_list[-1]                               # In Java, this would be `my_list.get(my_list.size() - 1)`

# Slicing can be used to access a subset of the list.
# my_list[0:2]                              # In Java, this would be `my_list.subList(0, 2)`
# This returns a new list containing the elements from index 0 to index 1 (inclusive).

# --------------------------------------------------
# Section 1: Tuples
# Tuples are immutable lists. They are used to store data that should not be changed. They are also faster than lists.
my_tuple = (1, 2, 3, 4, 5)                  # In Java, this would be `List<Integer> my_tuple = Arrays.asList(1, 2, 3, 4, 5)`
# my_tuple[0]                               # In Java, this would be `my_tuple.get(0)`
# my_tuple[0:2]                             # In Java, this would be `my_tuple.subList(0, 2)`
# my_tuple[0] = 0                           # This will throw an error because tuples are immutable.

# Negative indices can be used to access elements from the end of the tuple.
# my_tuple[-1]                              # In Java, this would be `my_tuple.get(my_tuple.size() - 1)`

# Slicing can be used to access a subset of the tuple.
# my_tuple[0:2]                             # In Java, this would be `my_tuple.subList(0, 2)`
# This returns a new tuple containing the elements from index 0 to index 1 (inclusive).

# --------------------------------------------------
# Section 2: Sets
# Sets are unordered collections of unique elements. They are used to test membership and eliminate duplicates.
#   They are also faster than lists. Hash tables are used to implement sets. Sets are mutable.
#sets have natural ordering. 
my_set = {-1,1, -3, 2, -4, 3,-2, 4, 5}                 # In Java, this would be `Set<Integer> my_set = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5))`
# my_set.add(6)                             # In Java, this would be `my_set.add(6)`
# my_set.remove(6)                          # In Java, this would be `my_set.remove(6)`
# my_set.clear()                            # In Java, this would be `my_set.clear()`
#pop takes most recent add and removes is # # (LIFO)LAST IN FIRST OUT. (FIFO)FIRST IN FIRST OUT      # In Java, this would be `my_set.remove(my_set.iterator().next())`
print (my_set)
name = my_set.pop()
print (name)
print (my_set.pop()) 
print (my_set.pop()) 
print (my_set.pop()) 
print (my_set.pop()) 
print (my_set)                     
# --------------------------------------------------
# Section 3: Dictionaries
# Dictionaries are Python's version of hash maps. They are mutable and can contain elements of different types.
#   They are unordered. Hash tables are used to implement dictionaries.
#my_dict = {"a": 1, "b": 2, "c": 3}          # In Java, this would be `Map<String, Integer> my_dict = new HashMap<>(); my_dict.put("a", 1); my_dict.put("b", 2); my_dict.put("c", 3);`
# print (my_dict["a"])                           # In Java, this would be `my_dict.get("a")`
# my_dict["d"] = 4                          # In Java, this would be `my_dict.put("d", 4)`
# print(my_dict)
# my_dict.pop("a")                          # In Java, this would be `my_dict.remove("d")`
# print(my_dict)
# my_dict.popitem()                         # In Java, this would be `my_dict.remove(my_dict.entrySet().iterator().next())`
# print(my_dict)
# my_dict.clear()                           # In Java, this would be `my_dict.clear()`

# --------------------------------------------------
# Section 4: Combining data structures
# Data structures can be combined to create more complex data structures. For example, a list of dictionaries.
my_list_of_dicts = [{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]
my_dict_of_sets = {"a": {1, 2, 3}, "b": {4, 5, 6}, "c": {7, 8, 9}}
my_set_of_tuples = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}

# --------------------------------------------------
# Exercise 1: Create a list called `my_list` and add the numbers 1 through 5 to it. Then, pass the list into a function
#   called `process_list`, which pops the last element from the list and prints it. Call the function 5 times.
# Exercise 2: Create a tuple called `my_tuple` and add the numbers 1 through 5 to it. Then, pass the tuple into a
# #   function called `process_tuple`, which prints first and last number in the tuple.
# Exercise 3: Create a set called `my_set` and add the numbers 1 through 5 to it.
#   Then pass the set to a function named 'create_dictionary' that creates a dictionary called `my_dict` with the
#   numbers of 'my_set' as keys and their squares as values. Return `my_dict` from the function.

# For these exercises, you may use the defined variables above. Also, be sure to annotate your functions with types.



# Uncomment the following lines to test your code after you have completed the exercises.
# process_list(my_list)
# process_tuple(my_tuple)
# create_dictionary(my_set)