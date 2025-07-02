# Part 1: Operations with Tuples, Lists, and Dictionaries

# Tuple operations
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("Tuple length:", len(my_tuple))
print("Tuple slice [1:3]:", my_tuple[1:3])

# List operations
my_list = [10, 20, 30, 40]
my_list.append(50)
print("List after append:", my_list) 
my_list.insert(2, 25)
print("List after insert:", my_list)
my_list.remove(20)
print("List after remove:", my_list)
print("List pop:", my_list.pop())
print("List after pop:", my_list)

# Dictionary operations
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)
my_dict['age'] = 26
print("Dictionary after update:", my_dict)
my_dict['country'] = 'USA'
print("Dictionary after adding key:", my_dict)
del my_dict['city']
print("Dictionary after deleting key:", my_dict)

# Part 2: Read data from a .c file and log to Excel

import os
import pandas as pd

# Specify the .c file path (update as needed)
c_file_path = 'sample.c'
excel_file_path = 'log_data.xlsx'

# Read lines from the .c file
if os.path.exists(c_file_path):
    with open(c_file_path, 'r') as file:
        lines = file.readlines()
    # Prepare data for Excel
    df = pd.DataFrame({'LineNumber': range(1, len(lines)+1), 'Content': [line.strip() for line in lines]})
    # Write to Excel
    df.to_excel(excel_file_path, index=False)
    print(f"Data from '{c_file_path}' has been logged to '{excel_file_path}'.")
else:
    print(f"File '{c_file_path}' not found. Please provide a valid .c file.")

