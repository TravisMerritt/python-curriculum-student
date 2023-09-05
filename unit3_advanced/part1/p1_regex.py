# Unit 3; Part 1: Using Regular Expressions
# Description: This file demonstrates how to use regular expressions in Python.

# -------------------------------
# Section 0: Introduction
# Regular expressions are a powerful tool for searching and manipulating text. They are supported in many programming
#   languages, including Python. Regular expressions are a language unto themselves, and are beyond the scope of this
#   course. However, we will cover the basics of how to use regular expressions in Python.
import re       # The re module is used for regular expressions.
my_string = "Hello, my name is John."
# Regular expressions are used to search for patterns in text. For example, if we wanted to search for the word "John"
#   in the string above, we could use the following regular expression:
pattern = "John"
matches = re.findall(pattern, my_string)
print(matches)

# With regular expressions, we can search for more than just a single word. For example, if we wanted to search for
#   any word that starts with the letter "J", we could use the following regular expression:
pattern = "J\w+"
matches = re.findall(pattern, my_string)
print(matches)
# The "\w" character matches any alphanumeric character, and the "+" character means "one or more". So, the regular
#   expression above will match any word that starts with the letter "J" and is followed by one or more alphanumeric
#   characters.

# -------------------------------
# Section 1: The re.match() Function
# The re.match() function is used to search for a pattern at the beginning of a string. For example, if we wanted to
#   search for the word "Hello" at the beginning of the string above, we could use the following regular expression:
pattern = "^Hello"
matches = re.match(pattern, my_string)
print(matches[0])
# re.match() will return groups of matches. In this case, there is only one match, so we can access it by using the
#   index 0. If there were multiple matches, we could access them by using the index 1, 2, etc.

# Capturing groups will allow us to access the individual groups of matches. For example, if we wanted to search for
#   the word "Hello" at the beginning of the string above, and then capture the rest of the string, we could use the
#   following regular expression:
pattern = "(\w+), (\w.+)"
matches = re.match(pattern, my_string)
print(f'First part: \"{matches[1]}\"; everything after the comma: \"{matches[2]}\"')

# -------------------------------
# Section 2: The re.search() Function
# The re.search() function is used to search for a pattern anywhere in a string. For example, if we wanted to search
#   for any word that begins with the letter "H", we could use the following regular expression:
# Generate a large body of text
my_string = "The quick brown fox jumps over the lazy dog."
pattern = "o\w+"
matches = re.search(pattern, my_string)
print(matches.groupdict())