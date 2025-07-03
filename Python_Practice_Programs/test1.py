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


student = {"Name":"ABC", "Roll_No": 11,"Age": 15, "Place": "Bangalore"}
students_data = {
    "student_1":{"Name":"Sanjay","Age": 23, "Roll_No": 14, "Place": "Bangalore"},
    "student_2":{"Name": "kalyan","Age": 28, "Roll_No":18, "Place": "Bangalore"}
}


for student_key, student_info in students_data.items():
    print(f"\n{student_key}:")
    for key, value in student_info.items():
        print(f"  {key}: {value}")