# pands-problem-sheet

This repository contains all weekly tasks for the Programming and Scripting module.

## Week 01 - helloworld.py

The file for this first week contains a simple program that prints 'Hello World!' when run. 

## Week 02 - bank.py

The file for this week contains a program that prompts the user for two money values in cents. 
Once the user enters these values, the program adds the two amounts and outputs in a readable format with a euro sign and decimal point.
We were instructed to only operate on the numbers as integers.

To avoid floating point numbers I had the program complete the mathematical operation, convert the result to a string, and separate the string into pre- and post-decimal parts. Once the string has been separated the two can be joined by a decimal place in the middle.

## Week 03 - accounts.py

The basic task for this week was to take a 10 character account number, and then output the number with only the last 4 digits displayed (first 6 being replaced by Xs).
There was an additional task to complete the same operation for account numbers of any/variable length.
I have split the program so that a user will first be asked for an account number of 10 characters, then an account number of any length. 

For the basic task I have split the input by keeping any digits other than the first 6. This will only work for an input of 10 digits to accurately display 6 Xs and 4 numbers.

For the Extra task I have made the assumption that the last 4 digits should always be visible, with everything else replaced by Xs. I ensure the correct number of Xs by subtracting 4 from the total length of the user input.

## Week 04 - collatz.py

The task for this week asked to create a program to execute the mathematical operations in the Collatz conjecture.
User is prompted for a positive integer input. The program then halves if number is even, multiplies by 3 and adds 1 if number is odd, and repeats these steps until output is 1.

An while loop was used to repeat the mathematical operations until the final output of 1.

Formatting of the output to match the requested output was done using the join() method found here: https://www.w3schools.com/python/ref_string_join.asp

## Week 05 - weekday.py

This program outputs whether the current day (the day the program is being run, not the day the program was written) is a weekday or weekend day.

I got information on how to acquire the current day from: https://www.w3schools.com/python/python_datetime.asp

I got some information on using if statements to check the contents of a list here: https://www.askpython.com/python/list/find-string-in-list-python

To accomplish this task I created a list of days and separated them into weekdays and weekend days. I then used an if statement to check which group the current day belongs to and output a response accordingly.

## Week 06 - squareroot.py

The task for this week was to create a program that takes a floating point number as the input, and outputs an approximation of its square root.

The recommendation for this was to look at the Newton method of estimating square roots. I got information on the Newton-Raphson method from: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

In the program I made an assumption about resolution (0.00000001) but this could have also been based on a user input. For the output I rounded to 1 decimal place to match the sample on course VLE but this could also have been based on user input.

The program itself repeats the mathematical formula x_i := (x_i+n/x_i)/2 until the solution squared differs from the initial, user input, value by less than or equal to the resolution.

## Week 07 - es.py

The program reads in a text file and outputs the number of e's it contains. I initially created this program to only read in lower case 'e' characters as that is the character specified on the VLE page. However, following feedback I have now expanded the program to also count upper case 'E' characters.

Info on command line arguments found here: https://realpython.com/python-command-line-arguments/
Info on searching text files found here: https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
Info on count() method found on w3 schools
Info on f.readlines() found here: https://www.w3schools.com/python/ref_file_readlines.asp

This program goes through the file line-by-line and counts the E and e character on each line, adding to the total.

This program takes the filename from a command line argument.

## Week 08 - plottask.py

This program generates 1000 normally distributed values (mean = 5, sd = 2) to plot on a histogram. It also plots x**3 on the same set of axes.

Information on normal distributions in numpy was found here: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

The x**3 plot was requested to be in the range [0, 10] and I have taken this to indicate 0 and 10 inclusive. This is why I used range(0,11)
