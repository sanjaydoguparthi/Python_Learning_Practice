print("\n create a set having with duplicate values")

var_set = {1, 3, 9, 8, 7, 1, 2, 3, 9, 2 } # create set with having duplicate values
print(var_set)
print(type(var_set))

print(" \n  create the list with duplicate variables")

var_list = [1, 3, 4, 5, 9, 8, 4, 1, 3, 2] # create list with having duplicate values
print(var_list)
print(type(var_list))

print(" \n list conversion to the set")

var_set_1 = set(var_list) # list to set conversion by using built in calss in python
print(var_set_1)
print(type(var_set_1))

print(" \n creat a tuple with duplicate variables")

var_tup = (9, 8, 7, 6,  1, 3, 9, 5, 3, 2, 2, 4)
print(var_tup)
print(type(var_tup))

print(" \n tuple conversion to the set")
var_set_2 = set(var_tup)
print(var_set_2)
print(type(var_set_2))

print("\n add one more variable")

var_set_3 = {1,2,4,5,6,7,8,3,9}
print(var_set_3)
print(type(var_set_3))
var_set_3.add(30)
print(var_set_3)

print("\n ")

#var_set_3.remove(40) #40 not present in the set due to so key error will come.
print("40 not present in the set")
var_set_3.add(30)
print(var_set_3)
var_set_3.remove(30)
print(var_set_3)

print(var_set_3.pop()) # to pop the first element from set
print(var_set_3.clear()) #To clear the set.

print("\n Membership in sets")

my_set_1 = {1,2,4,5,6,7,} # membership in set
print(my_set_1)
print(10 in my_set_1)
print(6 in my_set_1)


print("\n Mathematical operation")# mathematical operations
set_1 = {1,2,3,4,5,6,7}
set_2 = {5,6,7,8,9}
union_set = set_1.union(set_2) # combine the 2 sets of unique values
print(union_set)
union_set_1 = set_2.union(set_1)
print(union_set_1)

print(" \n  compare 2 sets of common lement ")

set_1 = {1,2,3,4,5,6,7}
set_2 = {5,6,7,8,9,3,4}

print(set_1)
print(set_2)
intersec_set = set_1.intersection(set_2) # common elements will get 
print(intersec_set)

set_1.intersection_update(set_2) # common elements update to set_1
print(set_1)
print(set_2)
set_2.intersection_update(set_1) # common elements update to set_2
print(set_2)

print(" \n ")

set_1 = {1,2,3,4,5,6,7,8,10,11}
set_2 = {5,6,7,8,9}
set_3 = {10,22,44,6,8,9}

print(set_2.difference(set_1)) # difference in set_2 will print when compared to set_1 is having common elements
print(set_2)
print(set_1.difference(set_2))
print(set_1)
print(set_1.difference(set_3))
print(set_1)
print(set_3.difference(set_1))
print(set_3)
print(set_1.difference(set_1))
print(set_1)
print(set_1.symmetric_difference(set_2)) # remove the common elements and print the unique elements.
print(set_1)

print(" \n ")

set_1 = {1,2,3,4,5,6,8,7}
set_2 = {6}
set_3 = {10,22,44,6,5,8}

print(set_2.issubset(set_1))
print(set_2.issubset(set_3))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))
print(set_3.issuperset(set_2))
