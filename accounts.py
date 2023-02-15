# accounts.py
# Reads in account numbers from user. 
# Then outputs the account number with all but the last 4 digits replaced with Xs.
# Author: Tom Brophy

# This section deals exclusively with 10 digit account numbers
account_number = input('Please enter a 10 digit account number: ')
last4 = account_number[6:]
print(f'XXXXXX{last4}')

#########################################################################

# This section deals with account numbers of varying length
# "Modify the program to deal with account numbers of any length"
# I have assumed here that the last 4 digits should always be visible, with everything else replaced by X.
# If there are less than 4 digits entered I have assumed all should be visible.
account_number2 = input('Please enter an account number of any length: ')
last4_varied = account_number2[-4:]
account_length = len(account_number2)
x_length = account_length-4
x_string = x_length*'X'
print(f'{x_string}{last4_varied}')