# format specifiers = {value:flags} format a value based on what flag are inserted

price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34
print(f"Price 1 is ${price_1:.2f}")
print(f"Price 2 is ${price_2:.1f}")
print(f"Price 3 is ${price_3:.of}")
print(f"Price 1 is ${price_1:10}")



# ,(number)f = round to that many decimal places (fixd point)
print(f"Price 1 is ${price_1:,.2f}")
print(f"Price 2 is ${price_2:,.2f}")
print(f"Price 3 is ${price_3:,.2f}")
# : spece (number)  = allocate that many spaces
print(f"Price 1 is ${price_1: }")
print(f"Price 2 is ${price_2: }")
print(f"Price 3 is ${price_3: }")

#  allocate and zero pad that many spaces
# :<         = left justify 
print(f"Price 1 is ${price_1:<10}")

# :>         = right justify
print(f"Price 1 is ${price_1:>10}")
# :^         = center align
print(f"Price 2 is ${price_2:^10}")
