decimal_number = int(input("Enter a Decimal Number: "))
choice = int(input("Choose a conversion:\n1. Binary\n2. Octal\n3. Hexadecimal\nEnter your choice: "))
if choice == 1:
    binary_number = bin(decimal_number)
    print("Binary Representation: ", binary_number)
elif choice == 2:
    octal_number = oct(decimal_number)
    print("Octal Representation: ", octal_number)
elif choice == 3:
    hex_number = hex(decimal_number)
    print("Hexadecimal Representation: ", hex_number)
else:
    print("Invalid Input, Please try again.")
