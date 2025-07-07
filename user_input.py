set_1 = {1,2,3,4,5,6,8,9}
set_2 ={5,6,7,8,9}
intersec_set = set_2.intersection(set_1) # common element
print(sorted(intersec_set))
'''
set_1.intersection_update(set_2) # common elemnts will update to set_1
print(set_1)
print(set_2)
set_2.intersection_update(set_1)# set_1 updated to set_1
print(set_1)
print(set_2)'''
