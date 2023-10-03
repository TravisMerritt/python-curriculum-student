# Unit 4, Part 2: Pandas
# Description: This file demonstrates how to use exception handling in Python.

# -----------------------------
# Import the necessary packages
# -----------------------------
import pandas as pd                 # pandas is a dataframe library (similar to R)
import numpy as np                  # numpy provides N-dim object support
import matplotlib.pyplot as plt     # matplotlib provides plotting functions

# -----------------------------
# Section 1: Reading data
# We have provided a CSV file called "nytimes front page.csv" in the res (resources) folder.
#   It contains all the front page headlines from the New York Times from 2015 to 2017.
data = pd.read_csv("res/nytimes front page.csv")    # read the data from the CSV file
print(f"Head:\n{data.head()}\n---\n")                       # print the first 5 rows of the data

# Note: If the file is taking a long time to load, you can use the following code to load only the first 100 rows:
# data = pd.read_csv("res/nytimes front page.csv", nrows=100)

# Pandas creates a dataframe object, which is similar to a table in a database. With this object, we can access and
# interpret the data in a variety of ways. If we want to access a specific column, we can use the following syntax:
print(f"Title column:\n{data['title']}\n---\n")             # print the "Headline" column

# If we want to access a specific row, we can use the following syntax:
print(f"First row:\n{data.iloc[0]}\n---\n")                 # print the first row

# If we want to access a specific cell, we can use the following syntax:
print(f"First cell:\n{data.iloc[0, 0]}\n---\n")             # print the first cell

# -----------------------------
# Section 2: Cleaning data
# Sometimes, a dataset will have missing values. We can use the following code to check for missing values:
print(f"Missing values:\n{data.isnull().sum()}\n---\n")     # print the number of missing values in each column

# We can use the following code to drop rows with missing values:
data = data.dropna()                                        # drop rows with missing values

# Other ways we can clean the data include:
#   - Removing duplicate rows
data = data.drop_duplicates()
#   - Removing rows with invalid values
data = data[data["title"].apply(lambda x: isinstance(x, str))]
#   - Removing rows with invalid data types
data = data[data["date"].apply(lambda x: isinstance(x, str))]
#   - Removing rows with invalid formats
data = data[data["date"].apply(lambda x: len(x) == 10 and x[4] == "-" and x[7] == "-")]
#   - Removing rows with invalid characters
data = data[data["title"].apply(lambda x: x.isascii())]
#   - Removing rows with invalid lengths
data = data[data["title"].apply(lambda x: len(x) > 0 and len(x) < 100)]
#   - Removing rows with invalid ranges
data = data[data["date"].apply(lambda x: int(x[0:4]) >= 2015 and int(x[0:4]) <= 2017)]

# -----------------------------
# Section 3: Analyzing data
# Now that we have cleaned the data, we can analyze it. We can use the following code to get the number of headlines:
print(f"Number of headlines: {len(data)}\n---\n")           # print the number of headlines

# We can use the following code to get the number of headlines per year:
headlines_in_2015 = len(data[data["year"] == 2015])
headlines_in_2016 = len(data[data["year"] == 2016])
headlines_in_2017 = len(data[data["year"] == 2017])

print(f"Number of headlines in 2015, 2016, 2017, respectfully: {headlines_in_2015}, {headlines_in_2016}, {headlines_in_2017}\n---\n")

# We can use the following code to get the number of headlines per month:
headlines_in_january = len(data[data["month"] == 1])
print(f"Number of headlines in January: {headlines_in_january}\n---\n")

# And, we can fetch the total number of front page headlines per month:
headlines_per_month = data.groupby("month").size()
print(f"Number of headlines per month:\n{headlines_per_month}\n---\n")

# To expand, we can calculate the average number of headlines per month using the following code:
average_headlines_per_month = headlines_per_month.mean()