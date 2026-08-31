## Ask user for their name
# name = input("What's your name? ")

## Say Hello to user
# print(f"Nice to meet you, {name}")

# print("Hello, " + name)

# print("Hello, ", end="")
# print(name)

# print("Hello, ", end="???")
# print(name)

# print("Nice meeting you, ", name, "!!!")

## Remove whitespace from str
# name = name.strip()

## Capitalize first letter
# name = name.capitalize()
# name = name.title()

# print(f"Nice meeting you, {name}")

"""Optimize the Code to Remove Extra Spaces and Capitalize Each Word"""
name = input("What's your name? ").strip().title()

## Split User's name into first and last name
first, last = name.split(" ")

print(f"Nice to meet you, {first}")
print(f"Your last name is {last}")