# format specifiers = {value:flags} format a value based on what flag are inserted

price_1 = 3.14159
price_2 = -987.65
price_3 = 12.34
print(f"Price 1 is ${price_1:.2f}")
print(f"Price 2 is ${price_2:.2f}")
print(f"Price 3 is ${price_3:.2f}")

print(f"Price 1 is ${price_1:.1f}")
print(f"Price 2 is ${price_2:.1f}")
print(f"Price 3 is ${price_3:.1f}")


print(f"Price 1 is ${price_1:.4f}")
print(f"Price 2 is ${price_2:.4f}")
print(f"Price 3 is ${price_3:.4f}")

print(f"Price 1 is ${price_1:.0f}")
print(f"Price 2 is ${price_2:.0f}")
print(f"Price 3 is ${price_3:.0f}")

print(f"Price 1 is ${price_1:10}")
print(f"Price 2 is ${price_2:10}")
print(f"Price 3 is ${price_3:10}")

print(f"Price 1 is ${price_1:010}")
print(f"Price 2 is ${price_2:010}")
print(f"Price 3 is ${price_3:010}")

# ,(number)f = round to that many decimal places (fixd point)
print(f"Price 1 is ${price_1:,.2f}")
print(f"Price 2 is ${price_2:,.2f}")
print(f"Price 3 is ${price_3:,.2f}")
# : spece (number)  = allocate that many spaces
print(f"Price 1 is ${price_1: }")
print(f"Price 2 is ${price_2: }")
print(f"Price 3 is ${price_3: }")

# : spece (number)  = allocate that many spaces
print(f"Price 1 is ${price_1: }")
print(f"Price 2 is ${price_2: }")
print(f"Price 3 is ${price_3: }")

# :03        = allocate and zero pad that many spaces
# :<         = left justify 
print(f"Price 1 is ${price_1:<10}")
print(f"Price 2 is ${price_2:<10}")
print(f"Price 3 is ${price_3:<10}")

# :>         = right justify
print(f"Price 1 is ${price_1:>10}")
print(f"Price 2 is ${price_2:>10}")
print(f"Price 3 is ${price_3:>10}")

# :^         = center align
print(f"Price 1 is ${price_1:^10}")
print(f"Price 2 is ${price_2:^10}")
print(f"Price 3 is ${price_3:^10}")

# :+         = use a plus sign to indicate positive value 
print(f"Price 1 is ${price_1:+10}")
print(f"Price 2 is ${price_2:+10}")
print(f"Price 3 is ${price_3:+10}")
print(f"Price 1 is ${price_1:,.2f}")
print(f"Price 2 is ${price_2:,.2f}")
print(f"Price 3 is ${price_3:,.2f}")

# :=         = place sign to leftmost position 
# :          = insert a space before positive numbers 
# :,         = comma separator 