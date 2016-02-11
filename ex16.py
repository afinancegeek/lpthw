# imports argument variable from system module
from sys import argv

# list of arguments including self
script, filename = argv

# prints file name that will be erased including the raw input (%r)
print "We're going to erase %r." % filename
# prints two options - erase file or not erase file
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# reads a line from input and converts what is read into a string
raw_input("?")
# opens a file and pulls some informaiton from it
# what is 'w' in this situation? 'w' is for writing to a file
print "Opening the file..."
# target is the variable that is used to open and write to the file
# that was creted (read = 'r', write = 'w', append = 'a')
# w + write plus something else
# a + append plus somehting else
target = open(filename, 'w')

# truncating removes all of the exisiting infromation from the file
print "Truncating the file. Goodbye!"
target.truncate()
# allows user to input 3 lines to the newly created or truncated file
# if a file hasn't already been created the programing will create one
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# write to target object that is defined earlier
target.write(line1)
# \n creates a line break	
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# closes file which is improtant because you might otherwise
# modify it by accident later when you acctualy don't mean to
print "And finally, we close it."
target.close()