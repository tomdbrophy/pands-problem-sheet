# bank.py
# Prompts users for money values in cents, adds those values, then outputs in human readable format with euro sign a decmial.
# Author: Tom Brophy

amount1 = int(input('Enter amount1 (in cent): '))
amount2 = int(input('Enter amount2 (in cent): '))
total = amount1+amount2
#print(total)

totalString = str(total)
euros = totalString[:-2]
#print(euros)
tens = totalString[-2]
cents = totalString[-1]

totalString2 = euros+'.'+tens+cents
#print(totalString2)

print('The sum of these is €'+totalString2)
