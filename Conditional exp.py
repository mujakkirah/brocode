# conditional ecpression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on condition 
#                         # X if condition else Y

# Basic Example : X if condition else Y

number = -5 #5 
print("Positive" if number > 0 else "Negative") #X if condition else Y (X=number) (y=Negetive)

number = 6
result = "Even" if number % 2 else "ODD" #X if condition else Y (x="Even") (y= "ODD") (conditon= %2)
print(result)

number = 5
a = 6
b = 7
age = 25 #13 result print child
temperature = 30 # 20
user_role = "admin" #"guest"


max_number = a if a > b else b                # X if condition else Y
min_number = a if a < b else b                 # X if condition else Y
status = "adult" if age >= 18 else "Child"      # X if condition else Y
weather = "Hot" if temperature > 20 else "cold"
access_level = "Full access" if user_role == "admin" else "limited access" 

print(max_number)
print(min_number)
print(status)
print(weather)
print= (access_level)