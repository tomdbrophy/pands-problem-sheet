# Takes in a user entered floating point number and outputs an approximation of its square root.
# Author: Tom Brophy
# Formula for Newton method of calculating square root found on hackernoon.com
# x_i := (x_i+n/x_i)/2
# Above formula should be repeatedly applied until x_i is a close approximation of squareroot.
# User should enter number to be solved.
# How close the result needs to be can be set in the code or could be also user entered.



def sqrt (number_to_solve, resolution = 0.00000001):
    x = number_to_solve
    while abs(x**2 - number_to_solve) > resolution:
        x = ((x+(number_to_solve/x))/2)
    return x    

val = float(input('Please enter a positive number: '))
answer = round(sqrt(val), 1)
print(f'The square root of {val} is approx. {answer}.')
