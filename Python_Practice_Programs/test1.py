lst = ["sanjay","kalyan","lalith kumar","vinay kumar","rahul"]# create a list
print(type(lst)) # type of list
print(lst)
lst.append('mahesh') #one more string attache in the list
print(lst)
lst.extend(['ashok']) # extenstion in the list
print(lst)

print(" \n positive indexing of the list ")
print("index[0]:",lst[0]) # positive indexing of the list 
print("index[1]:",lst[1])
print("index[2]:",lst[2])
print("index[3]:",lst[3])
print("index[4]:",lst[4])
print("index[5]:",lst[5])
print("index[6]:",lst[6])

print(" \n negetive indexing of list")
print("index[0]:",lst[0]) # positive indexing of the list 
print("index[-1]:",lst[-1])
print("index[-2]:",lst[-2])
print("index[-3]:",lst[-3])
print("index[-4]:",lst[-4])
print("index[-5]:",lst[-5])
print("index[-6]:",lst[-6])

print(" \n positive slicing of the list ")

print(lst[::2])
print(lst[::5])
print(lst[2::3])
print(lst[::3])
print(lst[2::4])

print(" \n negetive slicing of the list ")

print(lst[::-2])
print(lst[::-5])
print(lst[-2::-3])
print(lst[::-3])
print(lst[-2::4])




