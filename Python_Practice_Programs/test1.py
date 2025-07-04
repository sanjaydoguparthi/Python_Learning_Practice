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

## slicing list
numbers = [10, 20, 12, 13, 15, 9, 8, 7, 6]
print(numbers[::3])
print(numbers[::5])
print(numbers[2::])
print(numbers[::-1])

print(" \n  iterating our list ")
## iterating our list
for number in numbers:
    if number<6:
        print(number)
        
print(" \n iterating our list with index ")

 ##iterating with index
for index,number in enumerate(numbers):
    print(index,number)
    
print(" \n iterating our list with index ")   
    
for i in range(len(numbers)):
    if(i < 6):
        print(i,numbers[i])
    else:
        print("Excess access from index")

print(" \n  iterating  our list with user input")        

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13]
for index,number in enumerate(numbers,start = 0):
    if(index < 5):
        print(index,numbers[index])
    else:
        print(index,"Out of indexing range")
