# imports argument variable from system variable
from sys import argv

# list of arguments including self
script, filename = argv

""""
sets txt to open file object ex15_sample.txt using the file type
.txt

"""
txt = open(filename)

# prints output filename using raw_input entered by user
print "Here's your file %r:" % filename
print txt.read()

"""
ask user for raw_input again and re-prints the filename
based on raw_input

"""
print "Type the filename again:"
file_again = raw_input ("> ")

# reopens file object ex15_sample.txt and re-prints filename

txt_again = open(file_again)

print txt_again.read()

