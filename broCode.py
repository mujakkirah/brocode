#string, integer, float, boolean

#string mixing with print function 

first_name= "Mujakkir"
food = "pizza"
email= "mujakkirar4@gmail.com"
print( f"Hello ! {first_name}")
print(f"You like {food}.")
print(f"Your email is :{email}")

#integer 
age= 25
quantity = 3
num_of_students = 30
print(age)
print(f"you are {age} yrars old.")
print(f"you are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

#float / decimal point number 
price= 10.99
GPA= 3.2
distance = 5.5
print(f"The price is $ {price}.")
print(f" Your GPA is:{GPA}")
print(f" You ran {distance}km")


# type check 
name = "Mujakkir"
name= bool(name)
age = 25
GPA = 3.2
GPA=int(GPA) # use for type convert 

is_student = True
print(type(age))
print(type(name))
print(type(GPA))
print(type(is_student))
print(GPA)
print(name)

# use for some data input/ user input input() function ❓
name= input(" What is your name?: ")
age = int(input("How old are you?: "))
age= int(age)

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are { age} years old.")

# type changing 
length = int(input("Enter the length:"))
width = float(input("Enter the width:"))
area = length * width
print(f"this area is {area}")


# assignment operator 
friends = 0
friends = friends + 1
friends += 1
print(friends) 


friends= 5
#friends *= 3
#friends/=2
friends **= 2
print(friends)

friends= 10
remainder = friends % 2
print(remainder)

#some function 
x = 3.14
y = 4
z = 5
# result = round(x)
# result = int(x)
# result = float(x)
# result = abs(y)
#result = pow(4, 4)
result = max( x, y, z)
print(result)

# import math

X = 9.1
import math 
#print(math.pi)
#print(math.e)
#result = math.sqrt(X)
#result = math.ceil(X)
result = math.floor(X)

print(result)


# A=2 pi r
import math
radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f"The circumference is :{round(circumference)}")


# math.pi
radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f"The circumference is :{circumference}")


# math.sqrt
# i imagine it's a 📐 

import math 
a = float( input("Enter side A:"))
b = float( input("Enter side B:"))
c = math.sqrt (pow(a, 2) + pow(b, 2))
print(f"side C ={c}")

# if else and elif statement 

age = int(input("Enter your age :"))

if age >= 18:
    print("You are now singned up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up")
else:
    print( "you must be 18+ to sign up")



# if statement with boolen data 

for_sale = True

if for_sale:
    print("This item for sale")
else:
    print("This item is not for sale")