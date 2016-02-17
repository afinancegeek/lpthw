# imports the argument variable from the system module
from sys import argv
# states argument variable as being equal to itself and the input file
script, input_file = argv
# states that print_all is a function of f
# prints everything that's in f (a variable representing the file)
def print_all(f):
	print f.read()
# function goes to the beinging of the file
# 0 represents the bytes at which the file will rewind to
# seek tells the computer where to begin the document based on byte count
# file function is used to  tell the computer wether to read, write, or append
def rewind(f):
	f.seek(0)
# prints the two arguments on one line (line_count and f.read() )
# f is the file that we want printed
# line count is the number we want to read
# readline is a built in function method
def print_a_line(line_count, f):
	print line_count, f.readline()
# sets current file to the file that we input in the command line
current_file = open(input_file)

print "First let's print the whole file:\n"
# prints the current file that is also which is the same as the input file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# goes back to 0 bytes from the input or current file
rewind(current_file)

print "Let's print three lines:"
# print_a_line is a function that is based on the read line function
# it tells the computer to print one line at a time starting from the point that we set earlier in the exercise
# when we move from one like to the next we are incrementing the variable

current_line = 1
print_a_line(current_line, current_file)

# Re-Write -> current_line += current_line
current_line = current_line + 1
print_a_line(current_line, current_file)

# Re-Write -> current_line += current_line
current_line = current_line + 1
print_a_line(current_line, current_file)



