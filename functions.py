####Function is a block of code that runs only when called

def adding(num1, num2):
    x = num1+num2
    print(x)

adding(2,4)


#####Multiplication

def multiplication():
    num1 =12
    num2 =34
    sum = num2*num1
    print(sum)

multiplication()

##arguments
def courses(*args):
    for subject in args:
        print(subject)
courses('IT', 'Nutririon', 'Math')

def courses(*args):
    for subject in args:
        return subject
        print(courses('IT', 'Nutririon', 'Math'))


##keyword arguments

def cars(**kwargs):
    for key, value in kwargs.items():
        print("{}:{} ". format(key,value))

cars( car1='Subaru\n', car2='Bentley\n', car3='jeep')


##Default parameter value - used when we call the fn without an argument

def shoes(shoe_type = 'Airmax'): ##Airmax is set to be the default argument
    print('\nMy shoe type is ' + shoe_type )

shoes() ##this will print 'My shoetype is Airmax since it is the default parameter'
shoes('fila')
shoes('puma')



###passing a list as arguments

def  muFunction (devices):
    for x in devices:
        print(x)

input_devices = ['Keyboard', 'touchscreen', 'mouse']

muFunction(input_devices)


###passing a dictionary as arguments

def  muFunction (student):
    for x in student:
        print(x)
student = {
    'Fname' : 'James', #string
    'Sname' : 'Bond', #string
    'Tel' : 8508447, #integer
    'Shoes' : ['Fila', 'Airmax' , 'Dior'], #list
    'Male' : True

}

muFunction(student)

###The pass statement



###area of a circle
def area_of_circle():
    print('\nAREA OF A CIRCLE')
    pi = 3.142
    r = float(input('\nEnter the radius: '))
    area = (pi*r*r)
    print('\nThe area is ' + str(area))

area_of_circle()


###volume of a cylinder
def volume_of_cylinder():
    print('\nVOLUME OF A CYLINDER')
    pi = 3.142
    r = float(input('\nEnter the radius: '))
    h = float(input('\nEnter the height: '))
    v = (pi*r*h)
    print('\nThe volume is ' + str(v))
volume_of_cylinder()

###GRADING SYSTEM
def grading():
    mat = float(input('Enter marks for Math: '))
    sci = float(input('Enter marks for Science: '))
    eng = float(input('Enter marks for English: '))

    sum = mat+sci+eng
    avr = sum/3

    if avr >=0 and avr<=49:
        print('Average = ' + str(avr) + 'GRADE : E')
    elif avr >=50 and avr<=59:
        print('Average = ' + str(avr) + 'GRADE : D')
    elif avr >=60 and avr<=69:
        print('Average = ' + str(avr) + 'GRADE : C')
    elif avr >=70 and avr<=79:
        print('Average = ' + str(avr) + 'GRADE : B')
    elif avr >=80 and avr<=100:
        print('Average = ' + str(avr) + 'GRADE : A')
    else:
        print('Marks out of range! ')
grading()