student = {'name': 'doguparthi sanjay','register num': '20bj5a0464','branch': 'ECE','year of joining':2020}
student.update({'country': 'india'})
student['city'] = 'chirala'
student.pop('branch')
student.popitem()
student['name']

print(student.items())
print(student.keys())
print(student.values())
print(student.copy())


## shalow copy
## mistake of shalow copy
student = {'name': 'doguparthi sanjay','register num': '20bj5a0464','branch': 'ECE','year of joining':2020}
student_1 = student

print(student)
print(student_1)

student_1['name'] = 'kalyan kumar'
student_1['branch'] = 'mechanical'

print(student)
print(student_1)

student['year of joining'] = 2021
student_1['age'] = 22

print(student)
print(student_1)

## shallow copy
student_2 = student.copy()

print(student_2)
print(student.copy())

student_2['name'] = 'lalith kumar'
student_1['name'] = 'vinay kumar'

print(student_2)
print(student_1)
print(student)

# iterating the dictionary keys
for key_1 in student_2.keys():
    print(key_1)

# iterating over the vlaues
for value in student_2.values():
    print(value)

# Iterating over keys and values pair
for key, value in student_2.items():
    print(f"{key}: {value}")

## create nested dictionaries
students_data = {
    'student_1':{'name': 'doguparthi sanjay','register num': '20bj5a0464','branch': 'ECE','year of joining':2020},
    'student_2':{'name': 'doguparthi sanjay','register num': '20bj5a0464','branch': 'ECE','year of joining':2020}
}

print(students_data)
print(student.items())

# Iterating over nested dictionaries
for student_key, student_info in students_data.items():
    print(f"\n{student_key}:")
    for key, value in student_info.items():
        print(f"  {key}: {value}")

#iterative on nested disctionaries

for student_id, students_info in students_data.items():
    print(f"{student_id}:{students_info}")
    print(students_info.items())
    for key, value in students_info.items():
        print(f"{key}:{value}")

# Dictionary comprehensions examples
numbers = {x:x**2 for x in range(10)}
list_int = [x**2 for x in range(10)]
tuple_int = tuple(x**3 for x  in range(10))

print(numbers)
print(list_int)
print(tuple_int)

# Practical example of dictionary

# Use a dictionary to count the frequency of elements in the list.

numbers = [1,2, 3, 2, 4, 2, 1, 3, 4, 5, "Sanjay","kalyan",'sanjay','kalyan']
frequency = {}

print(type(frequency))

for num in numbers:
    if num in frequency:
        frequency[num]+=2
        print(frequency)
    else:
        frequency[num] = 1
        print(frequency)

print(frequency)

# use a dictionary to count the frequency of element in the list
numbers = [1,2, 3, 2, 4, 2, 1, 3, 4, 5, "Sanjay","kalyan",'sanjay','kalyan']
frequency = {}

print(type(frequency))

for num in numbers:
    if num in frequency:
        frequency[num]-= 2
        print(frequency)
    else:
        frequency[num] = 1
        print(frequency)

print(frequency)
    
    # use a dictionary to count the frequency of element in the list
numbers = [1,2, 3, 2, 4, 2, 1, 3, 4, 5, "Sanjay","kalyan",'sanjay','kalyan']
frequency = {}

print(type(frequency))

for num in numbers:
    if num in frequency:
        frequency[num]/= 2
        print(frequency)
    else:
        frequency[num] = 1
        print(frequency)

print(frequency)

 # use a dictionary to count the frequency of element in the list

numbers = [1,2, 3, 2, 4, 2, 1, 3, 4, 5, "Sanjay","kalyan",'Sanjay','kalyan']
frequency = {}

print(type(frequency))

for num in numbers:
    if num in frequency:
        print(frequency[num]!= 2)
        print(frequency)
    else:
        frequency[num] = 2
        print(frequency)

print(frequency)
