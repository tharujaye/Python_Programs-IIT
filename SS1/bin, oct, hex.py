decimal_num = int(input("Enter an integer: "))
binary_num = bin(decimal_num)[2:]
octal_num = oct(decimal_num)[2:]
hexadecimal_num = hex(decimal_num)[2:]

print("The binary representation of", decimal_num, "is:", binary_num)
print("The octal representation of", decimal_num, "is:", octal_num)
print("The hexadecimal representation of", decimal_num, "is:", hexadecimal_num)
