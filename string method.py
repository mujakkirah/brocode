name = input("Enter your full name: ")
phone_number = input("Enter your phone number #: ")
#result = len(name) # This function are totel count full name of word
#result = name.find("k")
#result = name.rfind("k")
#result = name.find("h")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()  # True or False 123 hole true abcd hole false
#result = name.isalpha() #abcdef = True , abc cd= false #abcd123=False
phone_number.count("-") #how many charecter in the string input exp 1-234-567-
phone_number = phone_number.replace ("-"," ")                     #replace Method ("-" "")
#print(result)
#print(name)
print(phone_number)