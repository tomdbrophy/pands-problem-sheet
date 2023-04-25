# collatz.py
# Asks user to enter a positive integer.
# If integer is even, halves number.
# If integer is odd multiply by 3 and add 1.
# Author: Tom Brophy
# Information on output formatting found here: https://www.w3schools.com/python/ref_string_join.asp


values = []
value = int(input('Please enter a positive integer: '))

while value != 1:
    if (value % 2) == 0:
        values.append(str(int(value)))
        value = value/2
    else:
        values.append(str(int(value)))
        value = (value*3)+1
values.append(str(int(value)))
print(' '.join(values))