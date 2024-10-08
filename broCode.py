#string, integer, float, boolean

#string
first_name= "Mujakkir"
food = "pizza"
email= "mujakkir485@gmail.com"
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

#float (codeing number )
price= 10.99
GPA= 3.2
distance = 5.5
print(f"The price is $ {price}.")
print(f" Your GPA is:{GPA}")
print(f" You ran {distance}km")

name = "Mujakkir"
name= bool(name)
age = 25
GPA = 3.2
is_student = True
GPA=int(GPA) # float data ke integer koarar system

print(type(age))
print(type(name))
print(type(GPA))
print( type( is_student))
print(GPA)
print(name)

#intup() = A function that prompts the user to enter data returns the entered as a string
input()
input("What is your name ?:")
name= input("What is your name ?:")
input("How old are you?:")

name= input(" What is your name?: ")
age = int(input("How old are you?:"))
age= int(age)
age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are { age} years old.")

# Excercise 1 Rectangle  area calc
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area = length * width
print(area)

#length = input("Enter the length:")
#width = input("Enter the width:")
#area = length * width
#print(area)

length = float(input("Enter the length:"))
width = float(input("Enter the width:"))
print(f"The area is : {area}cm²")
area = length * width

# Excercise 2 Shopping cart program
item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like"))
total = price * quantity
print(total)

# Excercise 2 Shopping cart program
item = input("What item would you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like"))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is : ${total}")

# Madlibs game
# word game where you create a story 
# by filling in blanks with random words.

adjective1= input("Enter an adjective ( description):")
noun1= input("Enter a noun ( person , place , thing):")
adjective2= input("Enter an adjective ( description):")
verb1 = input( "Enter  a verb ending with 'ing' " )
adjective3= input("Enter an adjective ( description):")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1} ")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

friends= 0
#friends = friends + 1
#friends += 1
#friends = friends -2
friends -= 2
print(friends)

friends= 5
#friends= friends * 3
#friends *= 3
#friends = friends/2
#friends/=2
#friends = friends ** 2
friends **= 2
print(friends)

friends= 10
remainder = friends % 2
print(remainder)

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

# math class
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


import math
radius = float(input('Enter the radius of a circle:'))
circumference = 2 * math.pi * radius
print(f"The circumference is :{circumference}")

#Math excercise 
import math
radius = float(input("Enter the redius of a circle:"))
area = math.pi * pow(radius, 2)
#print(f"The area of the circle is : { area }cm²")
#print(f"The area of the circle is : { round(area) }cm²")
print(f"The area of the circle is : { round(area, 2) }cm²")

#Math excercise  #Triangle 
import math 
a = float( input("Enter side A:"))
b = float( input("Enter side B:"))
c = math.sqrt (pow(a, 2) + pow(b, 2))
print(f"side C ={c}")

# if statement = Do some only IF some condition is True 
#               else do something else 
#age = int(input("Enter your age :"))
#if age >= 18:
 #   print("You are now singned up!")

#age = int(input("Enter your age :"))
#if age >= 18:
 #   print("You are now singned up!")
#else:
#    print( "you must be 18+ to sign up")

#age = int(input("Enter your age :"))
#if age >= 18:
#    print("You are now singned up!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#    print( "you must be 18+ to sign up")


age = int(input("Enter your age :"))
if age >= 18:
    print("You are now singned up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up")
else:
    print( "you must be 18+ to sign up")


response = input("Would yo like like food?(yes/no):")
if response == "yes":
    print("Have some food!")
else:
    print(("No food for you !"))

    name = input ("Enter your name: ")
if name == "":
    print("You did not type in your name")
else:
    print(f"Hello {name}")

    #Boolean if statment 
for_sale = True
if for_sale:
    print("This item for sale")
else:
    print("This item is not for sale")

online = True
if online:
    print("The user is online")
else:
    print("The user is offline")

online = False
if online:
    print("The user is online")
else:
    print("The user is offline")