# if condition with logical conditional operator 


# Logical operator = evaluate multiple condition (or, and, not)
#                   or = al least one conditon must be true
#                   and = both condition must be True
#                   not = inverts the condition (not False, not True)


# if and and conditon 

temp = -5
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT day")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("Its is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outsise")
    print("Its is sunny")


temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT day")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("Its is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outsise")
    print("Its is sunny")

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT day")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("Its is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outsise")
    print("Its is sunny")


# and not
temp = 28 # 0 , 20 and other 
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT Outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold outside")
    print("Its is sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outsise")
    print("Its is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT Outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside")
    print("Its is Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("Its is Cloudy")