# collection = single "variable" used to store multiple values
# List       = [] ordered and chanheble. Duplicates OK
# set        = {} unordered and immutable , but Add / Remove OK. NO duplicates 
# Tuple      = () ordered and unchangeable. Duplicates OK. FASTER 

fruit = "Apple" # collection 
fruits = ["Apple","Banana", "Orange","Mango"] #List
print(fruit)
print(fruits[-1]) # use for list indexing 

# now i use for Statement 
for x in fruits:
    print(x)

print(dir(fruits)) # dir convert dictionary 

print(help(fruits)) # help function 

print(len(fruits)) # len use for total number of elements 
print("apple" in fruit)

#fruits[1] = "pineapple"
#for fruit in fruits:
#    print(fruit)

#fruits.append("Pineapple")
#fruits.remove("Orange")
#fruits.insert(0, "Pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("Apple"))
print(fruits.count("Banana"))
print(fruits)