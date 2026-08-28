## Adding two Numbers
# x = 2
# y = 3

# z = x + y

# print(z)

## Convert Input to Integer
# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

### Alternative Way to Convert Input to Integer
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

""" Introducing Floats"""
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # To round off the answer to the nearest whole number
# z = round(x + y)  

# print(f"{z:,}")


## Division
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = (x / y)

# print(z)


## Round off Division
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x / y, 2)

# print(z)

"""Using F-String"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")