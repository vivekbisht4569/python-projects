'#!/usr/bin/env python3  -----> For Linux ' 
password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_symbol = False

for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_digit = True

    else:
        has_symbol = True


if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    print("Strong Password")

elif length >= 6 and (has_upper or has_lower) and has_digit:
    print("Medium Password")

else:
    print("Weak Password") 