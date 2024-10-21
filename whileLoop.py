# while loop = execute some code WHILE some condition remains true

# 📍
while age < 0:
    print("Age can't be negaive ")
    age = int(input("Enter your age: "))
print(f"you are {age} years old")

# 📍

food = input("Enter a food you like ( q for quit): ")
while not food =="q":
    print(f" You like {food}")
    food= input("Enter another food you like (q to quit): ")
print("Are you  don't like any food ?")

#📍
number = int(input("Enter a # between 1 - 10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input ("Enter a # between 1 - 10:"))
print(f"Your number is {number}")