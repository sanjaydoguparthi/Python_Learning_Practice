def person(**data):
    print(data)
    for k, v in data.items():
        if k == 'lastname':
            print(k, '    :', v)



i = 1
while i != '1':
    fname = input('enter your first name:')
    lname = input('enter last name:')
    age = input('enter your age:')
    mobileno = input('enter your mobile number:')
    print('')

    person(firstname=fname, lastname2=lname, age=age, mobile=mobileno)

    i = input('enter 0 to exit or any key to continue:')


persons = ['sanjay','kalyan','ashok','raviteja','rahul','avianash','vinay']
lengths = [len(person) for person in persons]
print(lengths)


skills = ['python','java','AWS cloud','linux','C++']
lengths = [len(skill) for skill in skills]
print(lengths)
