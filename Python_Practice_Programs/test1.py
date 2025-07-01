def add(num1,num2):  ##  add number of arguments
    result = num1+num2
    print('result :', result)
add(55,20)
add(60,40)
add(25,25)

def sayhello(name= 'user'):# function name as a argument
    print('hello',name)
    print('good morning')

user_name = ('avinash')
sayhello(user_name)
sayhello('sanjay')
sayhello('kalyan')
sayhello()