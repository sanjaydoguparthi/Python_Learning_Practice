## write afunction
def print_num(num):
    if num%2==0:
        print("print even number")
    else:
        print("print odd number")

("\n ")

print_num(25)

## default parameters
def greet(name):
    print(f"hello {name} welcome to the office")

greet('sanjay')

(" \n ")

###length of the function
## positional arguments
def print_name(*sanjay):
    for name in sanjay:
        print(name)

print_name('sanjay','vinay','harish','lalith kumar','ajay')

(" \n ")

##positional arguments
def print_number(*args):
    for number in args:
        print(number)

print_number(1,2,3,4,5,6,7,8)

(" \n ")

## keyword arguments
def print_student_data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_student_data(name = 'doguparthi sanjay', age = 24, date_of_birth = '04/08/2001', city = 'chirala' )

(" \n ")


## positional arguments and keyword arguments

def arguments_data(*args, **kwargs):
    for data in args:
        print(data)
       
    for key,value in kwargs.items():
        print(f" {key} : {value} ")
    
arguments_data(9,8,7,4,5, name = 'ajay', age = 20, city = 'chirala')
        





