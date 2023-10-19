decimal_number = int(input("Enter a decimal number: "))
choice = int(input("Choose conversion:\n1. Binary\n2. Octal\n3. Hexadecimal\nEnter your choice: "))
if choice == 1:
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
        print("Binary representation:", binary_number)
elif choice == 2:
    octal_number = ""
    while decimal_number > 0:
        octal_number = str(decimal_number % 8) + octal_number
        decimal_number = decimal_number // 8
        print("Octal representation:", octal_number)
elif choice == 3:
    hex_digits = "0123456789ABCDEF"
    hex_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hex_number = hex_digits[remainder] + hex_number
        decimal_number = decimal_number // 16
        print("Hexadecimal representation:", hex_number)
else:
    print("Invalid choice. Please try again")
