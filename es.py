# This program counts the number of times the letter 'e' occurs in a text file.
# A user should be able to specify the text file from the command line.
# Author: Tom Brophy
# Info on command line arguments found here: https://realpython.com/python-command-line-arguments/
# info on searching text files found here: https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
# Info on count() method found on w£ schools
# Info on f.readlines() found here: https://www.w3schools.com/python/ref_file_readlines.asp

FILENAME = 'dummy.txt'

def count_e():
    e_number = 0
    with open(FILENAME) as f:
        lines = f.readlines()
        for line in lines:
            es = line.count('e')
            e_number += es
    return e_number        

total = count_e()

#test = 'this that these and those'
#total = test.count('e')
print(total)